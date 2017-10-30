import unittest
import requests
import json
import tweepy


## SI 206 - HW
## COMMENT WITH: Sydney Hunt
## Your section day/time: Thursday 3-4PM
## Any names of people you worked with on this assignment:


## Write code that uses the tweepy library to search for var2 with three different phrases of the
## user's choice (should use the Python input function), and prints out the Tweet text and the
## created_at value (note that this will be in GMT time) of the first FIVE var2 with at least
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file
## along with your assignment.

## So, for example, if you submit your assignment files, and you have already searched for var2
## about "rock climbing", when we run your code, the code should use CACHED data, and should not
## need to make any new request to the Twitter API.  But if, for instance, you have never
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles"
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that
## contains your consumer_key, consumer_secret, access_token, and access_token_secret,
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information
## for an 'extra' Twitter account you make just for this class, and not your personal
## account, because it's not ideal to share your authentication information for a real
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these
## with variables rather than filling in the empty strings if you choose to do the secure way
## for EC points
consumer_key = "tSSmjXj2wUuJfFqneE1UylDfo"
consumer_secret = "Nalv8aGz8Hx4m5gzb25jx4xl8nDQcbll8EClfAz5LJXi5ri98K"
access_token = "464846788-UlDBvt3WK7bjxbRyhjDjG6Prw6eMxFxEIRnGTAFj"
access_token_secret = "7ZboZQwEpqJbJ5XfmW9wJ696m22zYLq0Oa8EsWkG5Xh1R"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except
## 		statement shown in class.
CACHE_FNAME = "cache_file.json"

try:
    cache_file = open(CACHE_FNAME, 'r') #opens file, reads contents
    cache_data = cache_file.read()  #reformats data into a string
    cache_dic = json.loads(cache_data) #sets up dict
    cache_file.close() #closing file
except:
    cache_dic = {}


## 2. Write a function to get twitter data that works with the caching pattern,
## 		so it either gets new data or caches data, depending upon what the input
##		to search for is.

def get_twitter_data(tweet):
    var1 = 'twitter_{}'.format(tweet)
    if var1 in cache_dic:
        print('Using Cache')
        return cache_dic[var1]
    else:
        print('Fetching')
        var2 = api.search(q=tweet)
        cache_dic[var1] = var2
        cached_dump_1 = json.dumps(cache_dic)
        var3 = open(CACHE_FNAME,"w")
        var3.write(cached_dump_1)
        var3.close
        return var2


## 3. Using a loop, invoke your function, save the return value in a variable, and explore the
##		data you got back!

for variable in range(3):
	var4 = input('enter tweet term: ') #enter tweet term
	var5 = get_twitter_data(var4)
	for item in var5["statuses"][:5]: #'statuses contains tweet info
		print("TEXT:",item["text"])
		print("CREATED AT:",item["created_at"])
		print("\n")
print("Complete")

## 4. With what you learn from the data -- e.g. how exactly to find the
##		text of each tweet in the big nested structure -- write code to print out
## 		content from 5 var2, as shown in the linked example.

for item in range(0, 3):
	var6 = input('enter tweet term: ')
	var7 = open(CACHE_FNAME, "r")
	var8 = json.load(var7)
	x = 0
	for item in var8[var6].keys():
		var9 = list(var8[var6].values())[x]
		print ('TEXT: ' + item)	#prints tweet
		print ('CREATED AT: ' + var9 + '\n') #prints additional information
		x += 1
