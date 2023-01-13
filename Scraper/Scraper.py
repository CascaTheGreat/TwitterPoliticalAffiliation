import json, os, re

def clean_tweet(prev):
    regs = [
        r'(\/\/www[^\s]+)',
        r'(pic.twitter.com\/[^\s]+)',
        r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',
        r'([\U00010000-\U0010ffff])',
        r'(?i)\b((?:https?:\/\/[^\s]+))',
        r'https',
        r'(/(\r\n)+|\r+|\n+|\t+/)',
        r'&amp;',
        r','
    ]
    for reg in regs:
        prev = re.sub(reg, " ", prev)
    if not prev.strip():
        return ("null")
    if prev[-1] == " ":
        prev = prev[:-1]
    return prev

def scrape(user):
    raw_tweets = []
    tweets = []
    f = open("user-tweets.json", 'r+')
    f.truncate(0)
    os.system(
        "snscrape --jsonl --max-results {} twitter-search 'from:{}'> user-tweets.json".format(100, user))
    for line in f:
      json_line = json.loads(line)
      raw_tweets.append(json_line)
    for tweet in raw_tweets:
        tweet = clean_tweet(tweet["renderedContent"])
        if tweet != "null":
            print(tweet)
            tweets.append(tweet)
    f.close()
    return (tweets)
scrape("ASCTEAlabama")