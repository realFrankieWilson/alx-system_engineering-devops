#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'User-Agent': 'Agent v2'
            }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    # json_obj = sub.json()
    if resp.status_code == 404:
        return 0
    data = resp.json().get('data')
    return data.get('subscribers')
