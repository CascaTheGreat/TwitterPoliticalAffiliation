import Scraper
import re


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
        return ("null")
    if prev[-1] == " ":
        prev = prev[:-1]
    return prev


def classify(user, num, pol):
    train_data = open("train_data.csv", "a+")
    tweets = Scraper.scrape(user, num)
    for tweet in tweets:
        tweet = clean_tweet(tweet)
        if tweet != "null":
            train_data.write('"{tweet}", {pol}\n'.format(tweet=tweet, pol=pol))