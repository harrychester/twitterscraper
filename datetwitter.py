import tweepy   #the twitter API library
import re       #regex library for extracting links
import datetime #to get the current and past date and time

TWITTER_BEARER_TOKEN = "<INSERT TOKEN HERE>"   #make a twitter development account to get one of these

USER = "GootLoaderSites"                    #add your user account here

f = open("malurl.txt", 'w+')                #opens a file to store whatever is being extracted from the tweet
count = 1                                   #I used a count varable to see how many tweets i was proccessing 
client = tweepy.Client(                     #this sets up the connection to twitter api
        bearer_token=TWITTER_BEARER_TOKEN)  #using the token defined before.
user_id = client.get_user(username=USER)    #gets the user id for the handle 
print(user_id)                              #I use this to get the id of the user as i couldnt be botthered to write code that extracted it from the mess twitter sends
user_id = 1280580986                        #once you run the code once with the line below unhashed put the ID here

#exit()                                     #unhash me to get user ID only and put it in the line below

tod = datetime.datetime.now()               #gets the current date and time
d = datetime.timedelta(days = 5)            #makes a time strucure of the time you enter (default is 5 days)
a = tod - d                                 #takes the time chosen away from the current time to get the time to start reading tweets from

tweets = client.get_users_tweets(user_id, max_results=100, start_time=a)  #gets 100 of the most recent tweets from the user
if not tweets.data:                     #if no tweets
        print("no new tweets")          #twitter bad, bad elon
        exit()                          #stops running

for tweet in tweets.data:               #for all the tweets collected
 
    urls = re.findall('hxxps?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', tweet.text)    #pull out all the links (the links im looking for are defanged) to get normal links change hxxps to https
  
    for url in urls:                    #for all the urls found in the tweet
        tmp = list(url)                 #converts to list
        tmp[1] = 't'                    #-}
        tmp[2] = 't'                    #-}-defanging [REMOVE if your not scraping defanged links]
        link = "".join(tmp)             #convert back to string
        f.write("\'" + link + "',")     #writes the link to the file opened earlier
