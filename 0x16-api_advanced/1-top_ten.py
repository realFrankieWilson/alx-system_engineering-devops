#!/usr/bin/python3
"""
A module that contains a method that quries the Reddit API
and print the top 10 titles of a given reddit subscriber
"""

import requests


def top_ten(subreddit):
    """
    Returns the number of subscribers for a given given subreddit
    """
    hder = {'User-Agent': 'User-Agent 2.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    limit = {'limit': 10}

    resp = requests.get(url, headers=hder, params=limit, allow_redirects=False)

    if not resp:
        print('None')
        return

    for sub in resp.json().get('data').get('children'):
        data = sub.get('data')
        title = data.get('title')
        print(title)
