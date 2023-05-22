#Bot for @QueeCrypto account!

import tweepy
from tweepy.auth import OAuthHandler

consumer_key = "OJ4vSsRtkHVcRwjgRQ6iJwaPJ"
consumer_secret = "Z5QUxuNZn6GW5or9Hk2nazTHIvMs37eHHmgRpcgBkOYL8OljIZ"
access_token = "1397504480816648196-LlYFpzKT8I5kUNdRtAv4O38TSZfYNi" #Normal1
access_token_secret = "UnkjHT87YzKwiUZeJMMlxycjz3mTdFTqBoxEYUSx2sxpG"  #Normal1 not v2 client

#Authenticate Twitter details
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

#Create an instance of the API class
api = tweepy.API(auth)

#Create a tweet
tweet = "The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth"
#tweet = "If you see this tweet, Smile \n\n While still smiling, follow @0xYongs to find more reasons to smile"
#tweet = "According to human beings, human beings are the smartest animals\n\n According to me, @0xYongs is the account to follow now!"

#Update a tweet
api.update_status(tweet + "\n\n $DIONE $CHNG $AZERO $FET $QNT $MNW $EWT $ROSE $METIS $RXD $RNDR $FRM $ROUTE $PYR")

api.update_status(tweet +" \n\n $SPY $NDX $IWM $QQQ $BTC $ETH $AAPL $TSLA $AMC $NFLX $UPST $PLTR $SNAP $FB $shib")

api.update_status(tweet + "\n\n $BTC $ETH $DOGE $XRP $ARB $LTC $BNB $SOL $POLYX $ADA $POLYX $OM $PERL $TORN $WIN $BTTC $CTSI $CFX $DEXE $CVC")
     
api.update_status(tweet + "\n\n $BTC $ETH $DOGE $ARB $XRP $SOL $BNB $LTC $AVAX $ID $OG $RNDR $AUDIO $TVK $AST $INJ $STEEM $AVAX $FET $PHA $LUNA $BLUR $APT $SOL $MATIC")
                                    
api.update_status(tweet + "\n\n $BTC $ETH $DOGE $XRP $ARB $LTC $BNB $SOL $POLYX $ADA $POLYX $OM $PERL $TORN $WIN $BTTC $CTSI $CFX $DEXE $CVC")

api.update_status(tweet + "\n\n $lunc #LUNC #bnb #bsc #binance #LuncBurn #lunccommunity $shib #shib #btc $btc #1000x $crypto $cryptocurrency $luncarmy $ETH $CREMAT $CREMATburn")

api.update_status(tweet + "\n\n $BTC $ETH $EGLD $XRP $ADA $DOGE $MATIC $SOL $DOT $AVAX $LINK $ICP $APT $HBAR $NEAR $CRO $ALGO")

api.update_status(tweet + "\n\n #gm #community #crypto $btc $bnb #DogeCola $eth $shib $doge #nft #bsc #memecoin")

print("Tweets updated for @CryptoQueen")
# 
# api.update_status("Name one awesome thing you will do today😎 '\n'Beside following @tradingsensei 👀 '\n''\n'  $STORY $celo $fil $eros $dino $xrp $mdx $zora $zoo $neo $doge $btc $sol $btcxec $eth $dai $qtum $pngn $mbox $bnb $eth")