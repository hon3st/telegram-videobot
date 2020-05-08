import requests
from requests_oauthlib import OAuth1

class TwitterApi:
  BASE_URL = 'https://api.twitter.com/1.1'

  def __init__(self, api_key, api_secret_key):
    self.api_key = api_key
    self.api_secret_key = api_secret_key
    self.oauth = OAuth1(self.api_key, self.api_secret_key)

  def get_tweet(self, id):
    url = self.BASE_URL + '/statuses/show/' + str(id) + '.json'
    return requests.get(url, auth=self.oauth).json()

