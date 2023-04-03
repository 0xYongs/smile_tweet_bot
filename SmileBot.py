from sys import api_version
import tweepy

#Authenticate Twitter details
auth = tweepy.OAuthHandler = ("CONSUMER_KEY" , "CONSUMER_SECRET")
auth.login_cred.OAuthHandler = ("ACCESS_TOKEN" , "ACCESS_SECRET")

#Create API object
auth = tweepy.API(auth)

#Create a tweet
api_version.status_update("Hello, I am back. I have missed you")