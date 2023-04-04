#Bot for @QueeCrypto account!

import tweepy
from tweepy.auth import OAuthHandler

consumer_key="OJ4vSsRtkHVcRwjgRQ6iJwaPJ"
consumer_secret="Z5QUxuNZn6GW5or9Hk2nazTHIvMs37eHHmgRpcgBkOYL8OljIZ"
access_token= "1397504480816648196-LlYFpzKT8I5kUNdRtAv4O38TSZfYNi" #Normal1
access_token_secret="UnkjHT87YzKwiUZeJMMlxycjz3mTdFTqBoxEYUSx2sxpG"  #Normal1 not v2 client

#Authenticate Twitter details
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

#Create an instance of the API class
api = tweepy.API(auth)
api = tweepy.API(auth)

#Create a tweet

#api_version.status_update("Hello, I am back. I have missed you")

api.update_status("Name one awesome thing you will do today😎 '\n'Beside following @tradingsensei 👀 '\n''\n' $link $VRA $btc $ada $dot $xrp  $SXP $bnb $atom $eth $ltc $kcs $aioz $theta $tfuel")

api.update_status("Name one awesome thing you will do today😎 '\n'Beside following @tradingsensei 👀 '\n''\n'  $STORY $celo $fil $eros $dino $xrp $mdx $zora $zoo $neo $doge $btc $sol $btcxec $eth $dai $qtum $pngn $mbox $bnb $eth")

api.update_status("Name one awesome thing you will do today😎 '\n'Beside following @tradingsensei 👀  '\n''\n'  $luna $rsr $bsc $rune $hnt $nano $reef $tel $kin $SXP $ $dash $knc $bnb $bat $doge $aave $xtz $xlm $xrp")

api.update_status("Name one awesome thing you will do today 😎 '\n'Beside following @tradingsensei 👀 '\n''\n'  $BTC $CHZ $ONT $XRP #ATH $MATIC $LTC $HOT #bsc $LOL $SXP $QTUM $DIA $COTI $FET $ROSE $CAKE")

api.update_status("Name one awesome thing you will do today 😎 '\n'Beside following @tradingsensei 👀 '\n''\n'  $BTC $ETH $CRV  $TP $USDC $bsc $SKL $SXP $HOT $ANKR $XVG $dot #SXP $ATH $SL $SAND $BTT $LTC $USDT $REAU $STC")

api.update_status("Name one awesome thing you will do today 😎 '\n'Beside following @tradingsensei 👀 '\n''\n'  $SPI $DOT $GRT $VSP $BTT $THETA #bsc  $SAND $CHZ $SPI $ONE $USDT $GLD $SLV $ABNB $bsc $SPOT")

api.update_status("Name one awesome thing you will do today 😎 '\n'Beside following @tradingsensei 👀 '\n''\n' $BTC $ADA $ETH $SL $BNB $HYDRA $SOL $dot $LOL $IT  $BART $TP $BSC $DCB $SXP $H $LTC $DOT $PT $RSI $ATH")

#api.update_status("Name one awesome thing you will do today '\n'Beside following @tradingsensei'\n''\n' $yongs `$link $VRA $btc $ada $dot $xrp  $SXP $bnb $atom $eth $ltc $kcs $aioz $theta $tfuel")
