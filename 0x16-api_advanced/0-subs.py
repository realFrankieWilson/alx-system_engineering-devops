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
    user_agent = 'User Agent'
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    headers = {'User-Agent': user_agent}

    resp = requests.get(url, headers=headers, allow_redirects=False)
    
    if resp.status_code != 200:
        return 0
    data = resp.json().get('data')
    return data.get('subscribers')
