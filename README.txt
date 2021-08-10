## ## Rasa Charbot Assignment - Restaurant Search Chatbot

## Group Facilotator : Sudip Kumar Sahu
## Email : sudipsahu17@gmail.com

## Group Member: Satish Bhoyar
## Email : getsatonline@gmail.com
#------------------------------------------------------------------------

### Problem Statement
#------------------------------------------------------------------------
An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. 
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

 
#### Inputs from the user:
#------------------------------------------------------------------------
1. City: Take the input from the customer as a text field
2. Cuisine Preference: Take the cuisine preference from the customer. The bot should list out the cuisine categories
3. Price range: Segment the price range into three price categories: lesser than 300, 300 to 700 and more than 700. 
	The bot should ask the user to select one of the three price categories. For example:

#### Output to the user:
#------------------------------------------------------------------------
While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average rating

Finally, the bot should ask the user whether he/she wants the details of the restaurants on email.
If the user replies 'yes', the bot should ask for user’s email id and then send it over email.
Else, just reply with a 'goodbye' message. The mail should have the following details for each restaurant:

1. Restaurant Name
2. Restaurant address
3. Average budget for two people
4. Rating

#### Goals :
1. NLU training: 
2. Build actions for the bot. 
3. Creating more stories.
4. Send mail to users
5. Deploy the model on Slack (Optional)

#-----------------------------------------------------------------------#
# To build the chatbot, we have done some modifications on top of it.
# Modifications are listed below :
	1. updated files -
		a. nlu.md - 
			i. More intents(deny, send_mail) added.
			ii. Added more examples for each intents
			iii. More synonyms are added  
			iv. Entities are updated
		b. stories.md
			i. All stories are updated
			ii. Interactive stories are added
		c. domain.yml
			i. More actions(utter) are added
			ii. Intents and Entities are updated
		d. actions.py
			i. More functions are added
			ii. Action classes are updated

