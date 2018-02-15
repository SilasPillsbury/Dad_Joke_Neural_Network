import urllib.request
import json
#import praw

def run(url = 'https://www.reddit.com/r/dadjokes/.json'):
  response = urllib.request.urlopen(url)
  jFile = response.read()

  data = json.loads(jFile)['data']
  for child in data['children']:
    if 'title' in child['data'].keys():
      print(child['data']['title'])
    if 'selftext' in child['data'].keys():
      print(child['data']['selftext'])
      print(' ')
  #children data selftext

run()

"""
def run2():
  r = praw.Reddit('searchandacrchive by ')

  subreddit_comment = r.get_comments(subName, limit=1000)
  subreddit_posts = r.get_submissions(subName, limit=1000)
"""
