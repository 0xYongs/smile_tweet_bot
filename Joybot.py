#Bot for @QueeCrypto account!

import tweepy
#from tweepy.auth import OAuthHandler

api_key = "bQpiFZmwG83AmDSmlI7Dvu3Kp"
api_secret = "V6oNeHWpLSKYD78ihZjMqByBwu6cRQwfvlbXg6MWjdj12BCB4d"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAECDpwEAAAAA0EX6v404A6AgaHjPL5cj3dubJfM%3DLfoKTEkZm3cxzAM6a9ELzCXCQOc0x96trEMjmo7hWuzPeqIiMe"
access_token = "1397504480816648196-GGRTnWrG1NIn0iyyheeScYX7kcA51I" #Normal1
access_token_secret = "a3lq1AYc4FrqAbERsjAavxSAQBQ9WaBo4Lc44yNBiGlu8"  #Normal1 not v2 client

# Gaining access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

#Authenticate Twitter details
auth = tweepy.OAuthHandler(api_key , api_secret)
auth.set_access_token(access_token , access_token_secret)

#Create an instance of the API class
api = tweepy.API(auth)

#Create a tweet
tweet = "The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth"
#tweet = "If you see this tweet, Smile \n\n While still smiling, follow @0xYongs to find more reasons to smile"
#tweet = "He trades, he codes and he creates \n\nAs if pridicting the last bull run was not enough. \n\nHe plans to do it again, he's @0xYongs"
#tweet = "According to human beings, human beings are the smartest animals\n\n According to me, @0xYongs is the account to follow now!"

# Creating a tweet to test the bot
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n #UFC293 #RWC2023 Izzy #GoForGold #Klipdrift #UseYourCashOnline Buthelezi Coco Strickland Laser ")
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n CONGRATULATIONS KHOSI TWALA Telkom Inkatha England Zulu Scotland Adesanya Morocco Giyani Shenge")
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n CHAPTER 26 WEEKEND George Ford Nigerians Blessed Sunday Argentina Namibia Mondli Makhanya Boipatong")
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n Dricus All Blacks Sabalenka Gauteng Dillon Brooks Safa tsatsii in soweto De Klerk Ireland MacG")
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n Ndlozi Southgate Takealot Chile Thokoza Calvin Trevor Chris Hani Mandela Japan Curry")
#client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth")
#client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth")
#client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth")
#client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth")
#client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth")