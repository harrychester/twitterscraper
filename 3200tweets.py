import tweepy   #the twitter API library
import re       #regex library for extracting links

TWITTER_BEARER_TOKEN = "<ADD TOKEN HERE>"   #make a twitter development account to get one of these

USER = "GootLoaderSites"                    #add your user account here

f = open("malurl.txt", 'w+')                #opens a file to store whatever is being extracted from the tweet
count = 1                                   #I used a count varable to see how many tweets i was proccessing 
client = tweepy.Client(                     #this sets up the connection to twitter api
        bearer_token=TWITTER_BEARER_TOKEN)  #using the token defined before.
user_id = client.get_user(username=USER)    #gets the user id for the handle 
print(user_id)                              #I use this to get the id of the user as i couldnt be botthered to write code that extracted it from the mess twitter sends
user_id = 1280580986                        #once you run the code once with the line below unhashed put the ID here

#exit()                                     #unhash me to get user ID only and put it in the line below

tweets = client.get_users_tweets(user_id, max_results=100)  #gets 100 of the most recent tweets from the user
tken = str(tweets[3])                   #this gets the last part of the received tweets which contains the token we need to get the next block of tweets
tkens = tken.split("_token': \'")       #-}
tkenss = tkens[1].split('\'')           #-}-extracts from this data the token
tken = tkenss[0]                        #-}

for tweet in tweets.data:               #for all the tweets collected
 
    urls = re.findall('hxxps?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', tweet.text)    #pull out all the links (the links im looking for are defanged) to get normal links change hxxps to https
  
    for url in urls:                    #for all the urls found in the tweet
        tmp = list(url)                 #converts to list
        tmp[1] = 't'                    #-}
        tmp[2] = 't'                    #-}-defanging [REMOVE if your not scraping defanged links]
        link = "".join(tmp)             #convert back to string
        f.write("\'" + link + "',")     #writes the link to the file opened earlier


for i in range(32):                         #run this 32 times
    tweets = client.get_users_tweets(user_id, max_results=100, pagination_token=tken)   #get the next block of tweets
    tken = str(tweets[3])               #-}
    tkens = tken.split("_token': \'")   #-}
    tkenss = tkens[1].split('\'')       #-}-same as above gets the token
    tken = tkenss[0]                    #-}
    if not tweets.data:                     #if it breaks
        print("token broke, twitter bad")   #twitter bad, bad elon
    else:                                   #if not broken
        for tweet in tweets.data:           #for each tweet in the block of tweets recieved
            urls = re.findall('hxxps?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', tweet.text)    #gets the links [same as above]

            for url in urls:        #
                tmp = list(url)             #-}
                tmp[1] = 't'                #-}
                tmp[2] = 't'                #-}- defanging [same as above]
                link = "".join(tmp)         #-}
                f.write("\'" + link + "',") # writes to the file opened before
            count += 1                      #adds 1 to the tweet count
print(count)                                #prints the amount of tweets processed