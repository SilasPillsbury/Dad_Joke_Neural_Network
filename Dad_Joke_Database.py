import urllib.request
import json

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
