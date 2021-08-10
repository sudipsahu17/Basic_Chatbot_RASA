## complete positive path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
	- slot{"cuisine": "chinese"}
	- slot{"price": "more than 700"}
	- slot{"check_resp": true}
	- utter_to_mail
* affirm
	- utter_ask_mail_id
* send_mail{"email": "anyone@gmail.com"}
    - slot{"email": "anyone@gmail.com"}
    - action_send_mail
	- slot{"email": "anyone@gmail.com"}
	- slot{"check_resp": true}
	- utter_mail_sent
	- utter_goodbye
	- export
	- action_restart
	
## no email path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
	- action_check_location
	- slot{"location": "kolkata"}
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
	- utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
	- slot{"cuisine": "south indian"}
	- slot{"price": "between 300 to 700"}
	- slot{"check_resp": true}
	- utter_to_mail
* deny
	- utter_goodbye
	- export
	- action_restart

## dont operate path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jhalda"}
    - slot{"location": "jhalda"}
	- action_check_location
	- slot{"location": "jhalda"}
	- slot{"check_resp": false}
    - utter_we_dont_operate
	- utter_goodbye
	- export
	- action_restart

## no restaurant path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"location": "mumbai"}
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "biryani"}
    - slot{"cuisine": "biryani"}
	- utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
	- slot{"cuisine": "biryani"}
	- slot{"price": "lesser than 300"}
	- slot{"check_resp": false}
	- utter_no_restaurant
	- utter_goodbye
	- export
	- action_restart

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
	- action_check_location
	- slot{"location": "hyderabad"}
	- slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
	- utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
	- slot{"cuisine": "north indian"}
	- slot{"price": "more than 700"}
	- slot{"check_resp": true}
	- utter_to_mail
* affirm
	- utter_ask_mail_id
* send_mail{"email": "anyone@gmail.com"}
    - slot{"email": "anyone@gmail.com"}
    - action_send_mail
	- slot{"email": "anyone@gmail.com"}
	- slot{"check_resp": true}
	- utter_mail_sent
	- utter_goodbye
	- export
	- action_restart

## location cuisine specified path 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"location": "mumbai"}
	- slot{"check_resp": true}
	- utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
	- slot{"cuisine": "chinese"}
	- slot{"price": "more than 700"}
	- slot{"check_resp": true}
	- utter_to_mail
* affirm
	- utter_ask_mail_id
* send_mail{"email": "anyone@gmail.com"}
    - slot{"email": "anyone@gmail.com"}
    - action_send_mail
	- slot{"email": "anyone@gmail.com"}
	- slot{"check_resp": true}
	- utter_mail_sent
	- utter_goodbye
	- export
	- action_restart

## location cuisine specified path 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Connor"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Connor"}
	- action_check_location
	- slot{"location": "Connor"}
	- slot{"check_resp": false}
	- utter_we_dont_operate
	- utter_goodbye
	- export
	- action_restart

## happy path 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "fast food", "location": "mumbai", "price": "between 300 to 700"}
	- slot{"location": "mumbai"}
	- slot{"cuisine": "fast food"}
	- slot{"price": "more than 700"}
	- action_check_location
	- slot{"location": "mumbai"}
	- slot{"check_resp": true}
	- action_search_restaurants
    - slot{"location": "delhi"}
	- slot{"cuisine": "chinese"}
	- slot{"price": "more than 700"}
	- slot{"check_resp": true}
	- utter_to_mail
* affirm
	- utter_ask_mail_id
* send_mail{"email": "anyone@gmail.com"}
    - slot{"email": "anyone@gmail.com"}
    - action_send_mail
	- slot{"email": "anyone@gmail.com"}
	- slot{"check_resp": true}
	- utter_mail_sent
	- utter_goodbye
	- export
	- action_restart
	
## happy path 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "fast food", "location": "mumbai", "price": "between 300 to 700"}
	- slot{"location": "mumbai"}
	- slot{"cuisine": "fast food"}
	- slot{"price": "more than 700"}
	- action_check_location
	- slot{"location": "mumbai"}
	- slot{"check_resp": true}
	- action_search_restaurants
    - slot{"location": "delhi"}
	- slot{"cuisine": "chinese"}
	- slot{"price": "more than 700"}
	- slot{"check_resp": false}
	- utter_no_restaurant
	- utter_goodbye
	- export
	- action_restart

## happy path 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "fast food", "location": "galaxy", "price": "between 300 to 700"}
	- slot{"location": "galaxy"}
	- slot{"cuisine": "fast food"}
	- slot{"price": "more than 700"}
	- action_check_location
	- slot{"location": "galaxy"}
	- slot{"check_resp": false}
	- utter_we_dont_operate
	- utter_goodbye
	- export
	- action_restart
	
## interctive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jhalda"}
    - slot{"location": "jhalda"}
    - action_check_location
    - slot{"location": "jhalda"}
    - slot{"check_resp": false}
    - utter_we_dont_operate
    - utter_goodbye
    - action_restart

## interctive_story_2
* greet
    - utter_greet
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - utter_ask_location
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_check_location
    - slot{"location": "faridabad"}
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Fast"}
    - slot{"cuisine": "Fast"}
    - action_search_restaurants
    - slot{"location": "faridabad"}
    - slot{"cuisine": "Fast"}
    - slot{"price": "more than 700"}
    - slot{"check_resp": true}
    - utter_to_mail
* affirm
    - utter_ask_mail_id
* send_mail{"email": "sudip@email.com"}
    - slot{"email": "sudip@email.com"}
    - action_send_mail
    - slot{"email": "sudip@email.com"}
    - slot{"check_resp": true}
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interctive_story_3
* restaurant_search{"price": "more than 700", "location": "nashik"}
    - slot{"location": "nashik"}
    - slot{"price": "more than 700"}
    - action_check_location
    - slot{"location": "nashik"}
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"location": "nashik"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "more than 700"}
    - slot{"check_resp": true}
    - utter_to_mail
* deny
    - utter_goodbye
    - action_restart

## interctive_story_4
* restaurant_search{"cuisine": "continental"}
    - slot{"cuisine": "continental"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_check_location
    - slot{"location": "ahmedabad"}
    - slot{"check_resp": true}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - slot{"cuisine": "continental"}
    - slot{"price": "between 300 to 700"}
    - slot{"check_resp": true}
    - utter_to_mail
* deny
    - utter_goodbye
    - action_restart

## invalid email path 1
* send_mail{"email": "anyone@gmail.com"}
    - slot{"email": "anyone@gmail.com"}
    - action_send_mail
	- slot{"email": "anyone@gmail.com"}
	- slot{"check_resp": false}
	- utter_mail_failed
	- utter_goodbye
	- export
	- action_restart

## invalid email path 2
* send_mail
	- utter_ask_mail_id
* send_mail{"email": "ghghaS@ASDSA.com"}
	- action_send_mail
	- slot{"email": "ghghaS@ASDSA.com"}
	- slot{"check_resp": false}
	- utter_mail_failed
	- utter_goodbye
	- export
	- action_restart

## interctive_story_5
* restaurant_search{"cuisine": "mughlai"}
    - slot{"cuisine": "mughlai"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_check_location
    - slot{"location": "hyderabad"}
    - slot{"check_resp": true}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "mughlai"}
    - slot{"price": "between 300 to 700"}
    - slot{"check_resp": true}
    - utter_to_mail
* affirm
    - utter_ask_mail_id
* send_mail{"email": "sudipsahu17@gmail.com"}
    - slot{"email": "sudipsahu17@gmail.com"}
    - action_send_mail
    - slot{"email": "sudipsahu17@gmail.com"}
    - slot{"check_resp": true}
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interctive_story_simple_1
* greet
    - utter_greet
* goodbye
    - utter_goodbye

## interctive_story_6
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Fast Food"}
    - slot{"cuisine": "Fast Food"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - slot{"cuisine": "Fast Food"}
    - slot{"price": "lesser than 300"}
    - slot{"check_resp": false}
    - utter_no_restaurant
    - utter_goodbye
    - action_restart

## interctive_story_7
* restaurant_search{"cuisine": "cafe", "location": "mumbai"}
    - slot{"cuisine": "cafe"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"check_resp": true}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "cafe"}
    - slot{"price": "between 300 to 700"}
    - slot{"check_resp": true}
    - utter_to_mail
* deny
    - utter_goodbye
    - action_restart

## interctive_story_8
* restaurant_search{"location": "kochi", "price": "lesser than 300"}
    - slot{"location": "kochi"}
    - slot{"price": "lesser than 300"}
    - action_check_location
    - slot{"location": "kochi"}
    - slot{"check_resp": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "dessert"}
    - slot{"cuisine": "dessert"}
    - action_search_restaurants
    - slot{"location": "kochi"}
    - slot{"cuisine": "dessert"}
    - slot{"price": "lesser than 300"}
    - slot{"check_resp": false}
    - utter_no_restaurant
    - utter_goodbye
    - action_restart

## interctive_story_9
* restaurant_search{"price": "more than 700", "cuisine": "cafe", "location": "mumbai"}
    - slot{"cuisine": "cafe"}
    - slot{"location": "mumbai"}
    - slot{"price": "more than 700"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "cafe"}
    - slot{"price": "more than 700"}
    - slot{"check_resp": true}
    - utter_to_mail
* affirm
    - utter_ask_mail_id
* send_mail{"email": "sudipsahu17@gmail.com"}
    - slot{"email": "sudipsahu17@gmail.com"}
    - action_send_mail
    - slot{"email": "sudipsahu17@gmail.com"}
    - slot{"check_resp": true}
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interctive_story_10
* restaurant_search{"price": "between 300 to 700", "cuisine": "fast food", "location": "kolkata"}
    - slot{"cuisine": "fast food"}
    - slot{"location": "kolkata"}
    - slot{"price": "between 300 to 700"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"check_resp": true}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - slot{"cuisine": "fast food"}
    - slot{"price": "between 300 to 700"}
    - slot{"check_resp": true}
    - utter_to_mail
* deny
    - utter_goodbye
