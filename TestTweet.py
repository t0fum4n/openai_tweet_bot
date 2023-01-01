import tweepy
import config


client = tweepy.Client(consumer_key=config.ck,
                       consumer_secret= config.cs,
                       access_token=config.at,
                       access_token_secret=config.ats)

# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text='hello world')

print(response)