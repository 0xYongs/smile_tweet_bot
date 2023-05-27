#Bot for @BerkyLazana acount!

import tweepy

consumer_key = "k2GamaYV4XieZrs2h5yfXStNM"
consumer_secret = "eTt3Q3CvPsXgVs1e9IKqITfMyK9h4Nb3g9l1AJjFDdGfeHQYt8"
access_token = "1431226236794281996-NMCM4nBrpNVngviwi3k0zLwG0YD0mY"
access_token_secret = "qbboIKhI6tQy6buDKDdfwAnuUHUjSyvhvmC3dEHHBaFFV"

#Authenticate Twitter details
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

#Create an instance of the API class
api = tweepy.API(auth)

#Create a tweet
tweet = "If you see this tweet, Smile \n\n While still smiling, follow @0xYongs to find more reasons to smile"
#tweet = "According to human beings, human beings are the smartest animals\n\n According to me, @0xYongs is the account to follow now!"
#tweet = "The bad news is 550 is not 225 \n\n The good news is you can follow @0xYongs for more truth"

#Update a tweet
api.update_status(tweet + "\n\n #coding #programming $COTI $LUNA $VER $LTC $BTC $VET $DOGE $XRP $VRA $ENJ $OCEAN $RUNE $MIR $BAND $HTR $TEL $HTR")

api.update_status(tweet +" \n\n #backend #opensource $ROOM $UMB $MATIC $DOT $ADA $BTC $LTC $AVAX $DOGE $PAID $HTR $CELL $LABS $FILE $KYL $ELON $ENJ $CHZ $WOLFY")

api.update_status(tweet + "\n\n $doge $eth $btc $ltc $fil $bnb $rsr $band $link $comp $dot $trb $uni $aave $sxp $sol $cake $sushi $xrp $alice $xvs $dot")
     
api.update_status(tweet + "\n\n $code $twt $bnb $sono $fyz $ori $lpnt $btc $inu $dgb $toc $ont $hbar $near $flow $rune $zec $ovi $dot $etc $tct $btc $lcg $hnt $snx $xem $ftm $xt")
                                    
api.update_status(tweet + "\n\n #dapp- #ai $polr $xtz $neo $pngn $ftm $qtum $rev $enj $aave $cvt $play $bbo $revo $icx $avax $sc $sx $trx $eos $slp $hodl $bch $tiki $posi $earn $nano")

api.update_status(tweet + "\n\n #dapp $qtum $ftt $trx $coco $inu $cws $nnb $tusd $pvu $xlm $sol $ctcn $slp $cro $rho $asp $yfi $zoo $egld $hnt $twt $crdt $atom $dsys $liq $rune")

api.update_status(tweet + "\n\n #womenintech $OCEA $RSR $VET $CHZ $FET $LUNA $LINK $DOT $ANKR $LTC $ETH $BTC $ADA $DOGE")

api.update_status(tweet + "\n\n #webdevelopment $BTC $ETH $XRP $DOT $KSM $LINK $GRT $CHR $SXP $COCOS  $AXS $DEGO $SKL $SUSHI $ZIL $MATIC $CHZ $ANKR $AKRO  $SHIB $DOGE")

print("Tweets updated for @berkylazana")