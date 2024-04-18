#!/usr/bin/python3
""" A script that queries a reddit api and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
  """ A function that returns the number of a reddit subscribers. """
  url = "http://www.reddit.com/r/{}/about.json"
  headers = {"User-Agent": "YourBot/1.0 by Frankiewilson"}
  resp = requests.get(url.format(subreddit), headers=headers, allow_redirects=False)

  if resp.status_code == 200:
    sub = resp.json().get("data").get("subscribers")
    return sub
  else:
    return 0
