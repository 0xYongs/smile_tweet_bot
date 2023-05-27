#Bot for @LisaBethlem

import tweepy
from tweepy.auth import OAuthHandler

consumer_key = "fiFhGjSgju8IwM6wcAp9QLbsX"
consumer_secret = "n2vPFRKll7harrpzVPeS2NYJxBwSlEJmlpUOo3v9RUDwZWvGf3"
access_token = "1431233607406956544-FTA9CgtCFJ30871VBzbMfylCkFDfwf"
access_token_secret = "u9PiQzZ8IoIFWU8sXIvzGoK0TGoqcCPoiDuzWRtCwcyVs"

#Authenticate Twitter details
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

#Create an instance of the API class
api = tweepy.API(auth)

#Create a tweet
#tweet = "According to human beings, human beings are the smartest animals\n\n According to me, @0xYongs is the account to follow now!"
tweet = "The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth"
#tweet = "If you see this tweet, Smile \n\n While still smiling, follow @0xYongs to find more reasons to smile"

#Update a tweet
api.update_status(tweet + "\n\n #ai $neko $cvag $axs $uft $xrp $aave $mobi $jsb $ely $near $bsp $coco $mola $ada $avax $dot $rune $rvn $air $mfi $cro")

api.update_status(tweet +" \n\n #pepe $wspp $hot $qdx $stx $nexo $snx $coco $dot $usdt $shib $cake $bcn $mina $dpet $xrp $qnt $bloc $bsv $crv $dcr $ltc $btcb")

api.update_status(tweet + "\n\n $bwx $aave $btt $chz $wspp $air $ada $egt $yfpi $gmx $pax $win $xem $fil $ksm $zoo $hop $mina $btg $amp $vntw $dcr $xdc")
     
api.update_status(tweet + "\n\n $ada $vgx $bree $chz $grt $dash $mkr $drgb $iotx $coco $flow $btg $bnb $bnb $sol $lpnt $vet $iotx $klay $zrx $ring $mby")
                                    
api.update_status(tweet + "\n\n $trx $reef $btc $dgb $grt $leo $enj $kcs $ada $pngn $zec $ht $hmt $soc $bnb $hbar $stx $doge $ftt $okb $grt $atom $sc")

api.update_status(tweet + "\n\n $algo $bwx $bec $shib $cel $zoo $mby $ethv $kcs $iotx $ring $egld $celo $usdt $grt $mkr $flow $okb $doge $dai $dgb $near")

api.update_status(tweet + "\n\n $clu $cake $mkr $ht $nexo $klay $xdc $chz $mis $ftt $coti $bnt $doge $axs $flow $lec $aave $enj $ust $slp $btt $bec $ftm")

api.update_status(tweet + "\n\n $play $aave $xlm $lec $okb $ust $mrcr $zil $egld $snx $rune $ht $eth $etc $sc $crv $pngn $bfc $dai $avax $ftm $ksm $dot")

api.update_status(tweet + "\n\n $vet $nano $klee $ada $iotx $mana $grt $axs $axs $ftt $hodl $zil $btt $bree $pngn $vgx $win $zec $lpnt $zoo $hmt $usdt")

print("Tweets updated for @LisaBethlem")