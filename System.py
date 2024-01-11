import tweepy
import configparser
import pandas as pd

# Read config.ini file
config = configparser.ConfigParser()
config.read('D:\\University Work\\GitHub\\FYP\\FYP-2023\\config.ini')

# Get Twitter API credentials from config.ini
consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_token_secret = config['access_token_secret']

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)


# Search for Formula 1-related tweets
query = 'Formula 1 -filter:media'
tweets = api.search_tweets(q=query, count=10)

# Prepare data for DataFrame
data = {'Screen Name': [tweet.user.screen_name for tweet in tweets],
        'Tweet': [tweet.text for tweet in tweets]}

# Create DataFrame
df = pd.DataFrame(data)

# Write DataFrame to CSV
df.to_csv('tweets.csv', index=False)


# # Print tweet text
# for tweet in tweets:
#     print(tweet.text)

