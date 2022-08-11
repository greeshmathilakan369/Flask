from cmath import isnan
import tweepy as tw
import pandas as pd 
import csv
import re


api_key="rje6cf6oiSh86DnSBisOzv9a3"
api_secret_key="5Q3eD834uEO36ojDEPaDfHOqnK4gkb86cNQjOSBiVg1e69m7fd"
#authentication
auth=tw.OAuthHandler(api_key,api_secret_key)
api = tw.API(auth, wait_on_rate_limit=True)
search_query = "#covid19 -filter:retweets"
# get tweets from the API



tweets = tw.Cursor(api.search_tweets,
              q=search_query,
              lang="en",
              since="2022-08-08").items(5)              

# store the API responses in a list

tweets_copy = []
for tweet in tweets:
    # print("tweets are...",tweet)
    tweets_copy.append(tweet)
        
    
print("Total Tweets fetched:", len(tweets_copy))

# .......dataframe creation of the above data

tweets_df=pd.DataFrame()
# for tweet in tweets_copy:
#     print(tweet)

#......
# populate the dataframe
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
    except:
        pass
    tweets_df = tweets_df.append(pd.DataFrame({'user_name': tweet.user.name, 
                                               'user_location': tweet.user.location,\
                                               'user_description': tweet.user.description,
                                               'user_verified': tweet.user.verified,
                                               'date': tweet.created_at,
                                               'text': text, 
                                               'hashtags': [hashtags if hashtags else None],
                                               'source': tweet.source}))
    tweets_df = tweets_df.reset_index(drop=True)

# ..................................Data description.............................................    
# show the dataframe

# print(tweets_df.head(70))
# print(tweets_df.isnull())
# print(tweets_df.isna().sum())
# print(tweets_df.dtypes)
tweets_df_new=tweets_df.drop(['user_verified','user_location','user_description','hashtags','source'],axis=1)
# print(tweets_df_new)

###for tweet in tweets_df_new:
###     if tweets_df_new[tweet].isnull !=True:


# #.......................Twitter Data Cleaning............................................
#1 ..........removing unwanted symbols.... convert to lower.......
clean_tweets=[]

# for tweet in tweets_df_new:                 
#     if tweets_df_new[tweet].isnull !=True:
#         for tweet in tweets_df_new['text']:
#             tweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([0-9])"," ",tweet)
#             tweet= tweet.lower()   #to lower
#             tweet=" ".join(tweet.split())  #to remove whitespaces btw text
#             clean_tweets.append(tweet)
#         tweets_df_new['text']=clean_tweets   
#         print(tweets_df_new) 

for tweet in tweets_df_new['text']:
  
    tweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([0-9])"," ",tweet)
    tweet= tweet.lower()   #to lower
    tweet=" ".join(tweet.split())  #to remove whitespaces btw text
    clean_tweets.append(tweet)
tweets_df_new['text']=clean_tweets  
print(tweets_df_new)  

# tweets_df_new.to_csv("tweet_greeshma_nnew.csv")

# #2....................removing white ..................

df=pd.read_csv("tweet_greeshma_nnew.csv")


# status....working second...on twitter_view.py