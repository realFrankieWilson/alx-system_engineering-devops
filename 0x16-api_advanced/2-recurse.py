#!/usr/bin/python3
"""
A module that contains a method that quries the Reddit API
and print the top 10 titles of a given reddit subscriber
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns list of titles containing all hot articles
    """
    hder = {'User-Agent': 'User-Agent 2.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    nxt = {'after': after}    # Next_page

    resp = requests.get(url, headers=hder, params=nxt, allow_redirects=False)

    if not resp:
        # print('None')
        return

    for sub in resp.json().get('data').get('children'):
        data = sub.get('data')
        title = data.get('title')
        hot_list.append(title)
    after = resp.json().get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
