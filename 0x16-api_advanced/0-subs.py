#!/usr/bin/python3
"""
A module that contains a method that returns a Reddit api
of the total number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {'User-Agent': 'User-Agent 2.0'}

    resp = requests.get(url.format(subreddit), headers, allow_redirects=False)

    if resp:
        data = resp.json().get('data').get('subscribers')
        return data
    return 0
