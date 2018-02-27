# importing the module
import tweepy
 
# personal details
consumer_key ="liV0bt6irtho0N8nASUvXuXhC"
consumer_secret ="XHjpE7l62Wy2iMnkY8J0GzJD3eJi9Pk5a5YnIDuDiUO9k8Xrvw"
access_token ="967252911196647424-hRcl5opCKEcjsTrX8jtuUrAm62OKCuu"
access_token_secret ="Kydk5SLqjBSXmAQIHjsFiDopDXQmw0DMQGqtUcirngVl1"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
