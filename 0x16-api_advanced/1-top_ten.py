#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def top_ten(subreddit):
    """Request top ten hot posts of subreddit
    from Reddit API
    """

    user_agent = '0x16-api_advanced'
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print('None')
    else:
        data = r.json()['data']
        section = data['children']
        for i in section:
            print(i['data']['title'])
