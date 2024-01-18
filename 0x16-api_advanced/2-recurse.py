#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after_val=None):
    """
    A recursive function that queries the Reddit API and retuns a list
    containing the titles of all hot artivlse for a given subeddit.
    """
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    subscribe = requests.get(
            api_url, allow_redirects=False, headers={
                'User-Agent': 'My User Agent 2.0'
                },
                params={
                'limit': 100,
                'after': after_val
                }
            )
    if  subscribe.status_code == 200:
        json_obj = subscribe.json()
        sub_access = json_obj.get('data').get('children')
        after_val = json_obj.get('data').get('after')

        for i in sub_access[:10]:
            hot_list.append(i.get('data').get('title'))

        if not after_val:
        	return (hot_list)

        return (recurse(subreddit, hot_list, after_val))

    return (None)
