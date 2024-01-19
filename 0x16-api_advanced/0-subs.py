#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given given subreddit
    """
    api_ = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    subscribe = requests.get(
            api_, allow_redirects=False, headers={
                'User-Agent': 'My User Agent 2.0'
                }
            )
    # json_obj = sub.json()
    if subscribe.status_code == 404:
        return 0
    return (subscribe.json().get('data').get('subscribers'))
