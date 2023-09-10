#Bot for @Benitoy1999 account!

import tweepy
from tweepy.auth import OAuthHandler

''' Update needed '''
consumer_key = "ZeIY2ue9V4tAlPneJaBs5bEqk"  
consumer_secret = "OGtPgdzmVCoU91Uj07cOzBpL7hij6dHF0oyodmrXROFy0KLR7x"

access_token = "1692892525801910272-cNZgAi9mWWfsciCgRuegELiAXDzPEI" #Normal1
access_token_secret = "ThbkCYEv82fCVMyrW24byMR5MbODixSD3gMTXhFRDksHk"  #Normal1 not v2 client

#Authenticate Twitter details
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

#Create an instance of the API class
api = tweepy.API(auth)

#Create a tweet
#tweet = "The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth"
#tweet = "If you see this tweet, Smile \n\n While still smiling, follow @0xYongs to find more reasons to smile"
tweet = "He trades, he codes and he creates \n\nAs if pridicting the last bull run was not enough. \n\nHe plans to do it again, he's @0xYongs"
#tweet = "According to human beings, human beings are the smartest animals\n\n According to me, @0xYongs is the account to follow now!"

#Update a tweet
api.update_status(tweet + "\n\n $DIONE $CHNG $PEPE $AZERO $FET $QNT $MNW #ALX_SE $ROSE $METIS $RXD $RNDR $FRM $ROUTE $PYR")

api.update_status(tweet + "\n\n $SPY $NDX $IWM $QQQ $PEPE $BTC $ETH $AAPL $TSLA $AMC $NFLX $UPST $PLTR $SNAP $FB $shib")

api.update_status(tweet + "\n\n $BTC $ETH $DOGE $XRP $PEPE $ARB $LTC $BNB $SOL $POLYX $ADA $POLYX #ALX_SE $PERL $TORN $WIN $BTTC $CTSI $CFX $DEXE $CVC")

api.update_status(tweet + "\n\n $BTC $ETH $DOGE $ARB $XRP $PEPE $SOL $BNB $LTC $AVAX $ID $OG $RNDR $AUDIO $TVK $AST $INJ $STEEM $AVAX $FET $PHA $LUNA $BLUR $APT $SOL $MATIC")
                                    
api.update_status(tweet + "\n\n $btc $STORY $celo $fil $eros $PEPE $dino $xrp $mdx $zora $zoo $neo $doge #ALX_SE $sol $btcxec $eth $dai $qtum $pngn $mbox $bnb $eth")

api.update_status(tweet + "\n\n $lunc #LUNC #bnb #bsc #binance $PEPE #LuncBurn #lunccommunity $shib #shib #ALX_SE $btc #1000x $crypto $cryptocurrency $luncarmy $ETH $CREMAT $CREMATburn")

api.update_status(tweet + "\n\n $BTC $ETH $EGLD $XRP $ADA $DOGE $PEPE $MATIC $SOL $DOT $AVAX $LINK $ICP $APT $HBAR $NEAR $CRO $ALGO")

api.update_status(tweet + "\n\n  $btc $bnb #DogeCola $eth $shib $doge $PEPE #nft #bsc #memecoin")

print("Tweets updated for @CryptoQueen")
# 
# api.update_status("Name one awesome thing you will do today😎 '\n'Beside following @tradingsensei 👀 '\n''\n'  $STORY $celo $fil $eros $dino $xrp $mdx $zora $zoo $neo $doge $btc $sol $btcxec $eth $dai $qtum $pngn $mbox $bnb $eth")