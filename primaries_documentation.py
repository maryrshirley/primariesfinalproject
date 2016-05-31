Using the Twitter search API, I want to understand if branded hashtag volume as a predictor of Democratic primaries. 

Background: How will social media relate to the outcomes of the democratic primaries? It’s not as ‘cool’ to be a supporter of Hillary - people are seemingly more vocal about Bernie.  but will this have any effects on the results of the primary?

Hypothesis: Whoever has a higher instance of branded hashtags will be likely to win that state’s primaries. 

Branded hashtags for democratic candidates: 
#imwithher vs #feelthebern


How I would do this: 
Use the Twitter Search API (https://dev.twitter.com/rest/public/search)
Search for #imwithher vs #feelthebern
Choose a geolocation of primary locations from June 7: California, Montana, New Jersey, New Mexico, North Dakota, South Dakota 
Use the URL encoder to set up the query 
Code - see pseudo code 
Create a set of functions to help define the count for hashtags for each candidate and decide whose is higher 
Correlation
Looking at the primary results, seeing if there is a correlation between the number of tweets and the results 

Dependencies: 
I would need to pull the API data on the day of the primaries (next Tuesday) and pull different geo locations for each of the 6 states that are having primaries. 
The data will be from the previous 7 days.

Whats included in this: 
Dictionaries 
API 
Parsing 
Functions 
Conditionals

Optional Other things to potentially look at: 
Positive/ negative 
Something about the candidates own tweets 
Some kind of negative/ positive #some kind of coding that looked at positive/ negative - like [no, hate, etc]