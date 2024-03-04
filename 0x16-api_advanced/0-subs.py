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
    header = requests.get(
        url, allow_redirects=False, headers={
            'User-Agent': 'My machin 1.0'
        }
        )
    resp = header.json()
    if header:
        return (resp.get('data').get('subscribers'))
    return (0)
