

def bern_list() #building a function to understand the popularity of Bernie hashtags in a state 
#Twitter API search data for #feelthebern 

	from urllib2 import urlopen
	from json import load
	apiUrl = "Insert Twitter API"

	#open the apiUrl and assign data to variable
	response = urlopen(apiUrl)

	json_obj = load(response)

	return json_obj #this will print a dictionary

def bern_count() #from the above, parse out one value so we can count it 
	ratings.keys() #this will print a list of all the keys in a dictionary - key is the hashtag #we may need to parse here 
	#Turn the dictionary into a list 
	[list].count('feelthebern')
	return count 

def hill_list() #building a function to understand the popularity of Bernie hashtags in a state 
#Twitter API search data for #feelthebern 

	from urllib2 import urlopen
	from json import load
	apiUrl = "Insert Twitter API"

	#open the apiUrl and assign data to variable
	response = urlopen(apiUrl)

	json_obj = load(response)

	return json_obj #this will print a dictionary

def hill_count() #from the above, parse out one value so we can count it 
	ratings.keys() #this will print a list of all the keys in a dictionary - key is the hashtag #we may need to parse here 
	#Turn the dictionary into a list 
	[list].count('imwithher')
	return count 

def who_won()
	if bern_count > hill_count:
		print "Bernie is more popular"
	else:
		print "Hillary is more popular"

if __name__ == '__main__':
    # Run the main execution flow here

#call everything here
