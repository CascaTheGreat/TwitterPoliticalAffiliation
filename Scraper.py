import json,os
def scrape(user,num):
  raw_tweets = []
  tweets = []
  f=open("user-tweets.json",'r+')
  f.truncate(0)
  os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> user-tweets.json".format(num, user))
  for line in f:
    json_line = json.loads(line)
    raw_tweets.append(json_line)
  for tweet in raw_tweets:
    tweets.append(tweet["content"])
  f.close()
  return(tweets)