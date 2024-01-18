#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Returns the the titles of the top ten posts of a given subreddit
    """
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    subscribe = requests.get(
            api_url, allow_redirects=False, headers={
                'User-Agent': 'My User Agent 2.0'
                }
            )
    if subscribe.status_code == 404:
        print("None")
        return
    json_obj = subscribe.json().get("data")
    [print(info.get("data").get("title")) for info in json_obj.get("children")]
