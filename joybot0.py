#Bot for @BerkyLazana acount!

import tweepy

api_key = "k2GamaYV4XieZrs2h5yfXStNM"
api_secret = "eTt3Q3CvPsXgVs1e9IKqITfMyK9h4Nb3g9l1AJjFDdGfeHQYt8"
bearer_token = "AAAAAAAAAAAAAAAAAAAAANaRTAEAAAAAoTEkq5LMJyU5U5QiHdiXmjtRSYY%3DplQF7xylxMLUhyUvy27h3OPSdoz4qFC0sYbbD8rqRmkvzgwM3K"
access_token = "1431226236794281996-NMCM4nBrpNVngviwi3k0zLwG0YD0mY"
access_token_secret = "qbboIKhI6tQy6buDKDdfwAnuUHUjSyvhvmC3dEHHBaFFV"

# Gaining access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

#Authenticate Twitter details
auth = tweepy.OAuthHandler(api_key , api_secret)
auth.set_access_token(access_token , access_token_secret)

#Create an instance of the API class
api = tweepy.API(auth)

#Create a tweet
#tweet = "If you see this tweet, Smile \n\n While still smiling, follow @0xYongs to find more reasons to smile"
#tweet = "According to human beings, human beings are the smartest animals\n\n According to me, @0xYongs is the account to follow now!"
#tweet = "The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth"
tweet = "He trades, he codes and he creates \n\nAs if pridicting the last bull run was not enough. \n\nHe plans to do it again, he's @0xYongs"

#Update a tweet
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n Dillon Brooks #sundayvibes #AskFFT NFL Sunday Good Sunday Go Birds #FlyEaglesFly Team USA #HereWeGo Mel Tucker ")
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n Football Sunday #DawgPound Izzy Who Dey Phoenixville Go Browns Game Day Mikal Bridges Who Dat Strickland ")
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n Blessed Sunday Shaheen Andrews Madoka Rohit Steve Kerr Homura Isaiah Likely Michigan State Gunna ")
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n Danelo Cavalcante Musgrave Higbee full ppr Tink Adesanya Auburn Airdrop Cleveland Browns Longwood Gardens")
client.create_tweet(text="The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth\n\n PEMDAS Redzone Stanford Stargate Mark Cuban Briles Barclays Ability Invictus Pereira")
print("Tweets updated for @berkylazana")