import Scraper
import re
from werkzeug.datastructures import ImmutableMultiDict
def score(tweet):
  lr_word_count = 1
  al_word_count = 1
  pol_scores = {"left": 0,"right": 0, "auth": 0, "liberal": 0}
  for dict_key in pol_scores:
    if dict_key == "left" or dict_key == "right":
      pol_scores[dict_key] /= lr_word_count
    else:
      pol_scores[dict_key] /= al_word_count
  print(pol_scores)
  return(pol_scores)
def clean_tweet(tweet):
    regs = [
        r'(\/\/www[^\s]+)',
        r'(pic.twitter.com\/[^\s]+)',
        #r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',
        r'([\U00010000-\U0010ffff])',
        r'(?i)\b((?:https?:\/\/[^\s]+))',
        r'https',
        r'(/(\r\n)+|\r+|\n+|\t+/)'
    ]
    prev = tweet
    for reg in regs:
        prev = re.sub(reg, " ", prev)
    if not prev.strip():
      return("null")
    if prev[-1] == " ":
      prev = prev[:-1]
    return prev
def classify(user,num,pol):
  train_data = open("train_data.csv","a+")
  tweets = Scraper.scrape(user, num)
  for tweet in tweets:
    tweet = clean_tweet(tweet)
    if tweet != "null":
      train_data.write('"{tweet}", {pol}\n'.format(tweet=tweet,pol=pol))