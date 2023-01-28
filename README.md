# twitterscraper
a python script that uses tweepy to pull tweets from a twitter user. 

#############################################################################################
3200tweets.py
#############################################################################################
this program gets 3200 (the max number twitter api lets you get) tweets from a user's account. the code does not work out the box unless you are scraping the same profile as me. 
if you want to scrape a different profile, go into the code and follow the comments to get the user ID and enter it into the code. 

the code is currently set up top retrieve defanged links from the tweets and refang them. these links will then be stored in a comma seperated list witheach item being in speech marks. 

to change the ammount of tweets pulled you can change the for loop that runs 32 times or the block size. all instructions on how to do this is in the code

#############################################################################################
