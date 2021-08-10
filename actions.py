from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import pandas as pd
import json
import smtplib
import traceback
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ZomatoData = pd.read_csv('zomato.csv', engine='python', index_col='Restaurant ID')
ZomatoData = ZomatoData.drop_duplicates()
WeOperate = ZomatoData.City.apply(lambda city : city.split(" ")[1] if " " in city else city).str.lower().unique().tolist()
serach_results = None

def checkCity(Location):
	loc = Location.strip().lower()
	if " " in loc:
		loc = loc.split(" ")[1]
	return loc

def ValidateLocation(Location):
	loc = checkCity(Location)
	if loc in WeOperate:
		return True
	else:
		return False

def RestaurantSearch(City, Cuisine, Price):
	City = checkCity(City)
	Cuisine = Cuisine.lower().strip()
	Price = Price.lower().strip()
	
	restaurant_df = ZomatoData[(ZomatoData.City.apply(lambda city : City in city.lower()))]
	if Cuisine != "all" and Cuisine != "any":
		restaurant_df = restaurant_df[(restaurant_df.Cuisines.apply(lambda cuisine : Cuisine in cuisine.lower()))]
	if Price == "more than 700":
		restaurant_df = restaurant_df[(restaurant_df['Average Cost for two'] > 700)]
	elif Price == "between 300 to 700":
		restaurant_df = restaurant_df[(restaurant_df['Average Cost for two'] > 300) &  (restaurant_df['Average Cost for two'] <= 700)]
	elif Price == "lesser than 300":
		restaurant_df = restaurant_df[(restaurant_df['Average Cost for two'] <= 300)]
	else:
		print ("Invalid Price Range -->", Price, "!!")
	restaurant_df = restaurant_df.sort_values(by='Aggregate rating', ascending=False)
	
	return restaurant_df[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]


def getHtmlText(ResultDF):
	total = len(ResultDF)
	text = """\
			<html>
				<head>
					<style>
					table, th, td {
					  border: 1px solid black;
					  border-collapse: collapse;
					}
					th, td {
					  padding: 5px;
					  text-align: left;
					}
					</style>
				</head>
				<body>
					<h2>Restaurant Details from ChatBot</h2></br>
			"""
	text += "<h4>We have found  " + str(total) + " serach results for you.</h4></br></hr>"
	text += """\
				<table>
					<thead>
						<tr>
							<th>#</th>
							<th>Restaurant Name</th>
							<th>Address</th>
							<th>Cost for Two</th>
							<th>Rating</th>
						</tr>
					</thead>
					<tbody>
			"""
	count = 1
	for index, row in ResultDF.iterrows():
		text += "<tr>"
		text = text + "<td>" + str(count) + "</td>"
		text = text + "<td>" + str(row['Restaurant Name']) + "</td>"
		text = text + "<td>" + str(row['Address']) + "</td>"
		text = text + "<td>" + str(row['Average Cost for two']) + "</td>"
		text = text + "</td>" + str(row['Aggregate rating']) + "</td>"
		text += "</tr>"
		count += 1
	text += "</tbody></table></br></hr>"
	text += "<h4>Have a good meal !! Thank you for visiting us !!</h4></body></html>"
	return text
	
def sendmail(MailID, Results):
	try:
		mail_content = getHtmlText(Results)
		sender_address = 'testforpython41@gmail.com'
		receiver_address = MailID.strip().lower()
		sender_pass = 'No17Lion'
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'Resturant Deatils - ChatBot'
		message.attach(MIMEText(mail_content, 'html'))
		session = smtplib.SMTP('smtp.gmail.com', 587)
		session.starttls()
		session.login(sender_address, sender_pass)
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		return True
	except:
		traceback.print_exc()
		return False

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		res = True
		try:
			results = RestaurantSearch(City=loc, Cuisine=cuisine, Price=price)
			response=""
			if results.shape[0] == 0:
				response = "Sorry, No Result Found !!"
				res = False
			else:
				global serach_results
				serach_results = results
				total_results = len(results)
				response = "We found " + str(total_results) + " results.\n"
				top_results = results
				if (len(results) >= 5):
					response += "Showing you top results:" + "\n"
					top_results = results.head(5)
					
				count = 1
				for index, row in top_results.iterrows():
					response = response + str(count) + ": Name - " +str(row['Restaurant Name']) + "\n"
					response = response + " : Address - " + str(row['Address']) + "\n"
					response = response + " : Cost for Two - Rs. " + str(row['Average Cost for two']) + "\n"
					response = response + " : Address - " + str(row['Aggregate rating']) + "\n\n"
					count += 1
					
			dispatcher.utter_message(response)
		except:
			traceback.print_exc()
			res = False
		return [SlotSet('location',loc), SlotSet('cuisine', cuisine), SlotSet('price',price), SlotSet('check_resp',res)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('email')
		res = sendmail(MailID, serach_results)
		return [SlotSet('email',MailID), SlotSet('check_resp',res)]

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		res = ValidateLocation(loc)
		return [SlotSet('location', loc), SlotSet('check_resp', res)]