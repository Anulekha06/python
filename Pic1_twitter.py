import os
import time
import tweepy
consumer_key='liV0bt6irtho0N8nASUvXuXhC'
consumer_secret='XHjpE7l62Wy2iMnkY8J0GzJD3eJi9Pk5a5YnIDuDiUO9k8Xrvw'
access_token='967252911196647424-hRcl5opCKEcjsTrX8jtuUrAm62OKCuu'
access_token_secret='Kydk5SLqjBSXmAQIHjsFiDopDXQmw0DMQGqtUcirngVl1'
#these are the keys and access secret codes for sending the tweet
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/cs2017a104/anitha/img"+str(b)+".jpg"
    cmd="fswebcam -r 1280x720 -S 3 --jpeg 100 "+img
    os.system(cmd)
    print("pic taken")
    #read image from location
    api.update_with_media(img, status="nice one")
    print("wait for 5 seconds for selfii!")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
