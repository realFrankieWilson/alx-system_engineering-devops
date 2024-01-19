#!/usr/bin/python3
"""
A module that contains a method that returns a Reddit api
of the subscribers activities
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the 10 hottest posts of a given subreddit
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 2.0'}
    sub_obj = requests.get(url, allow_redirects=False, headers=headers)

    if sub_obj:
        obj_file = sub_obj.json()
        res_data = obj_file.get('data').get('children')

        data_lists = []

        for i in res_data[:10]:
            data_lists.append(i.get('data').get('title'))

        for j in data_lists:
            print(j)
    else:
        print('None')
