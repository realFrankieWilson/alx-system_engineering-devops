#!/usr/bin/python3
"""
A module that queries a Reddit Api and returns title of all hot articles
"""
import requests


def count_words(subreddit, word_list, instances={}, after=None):
    """
    Counts and print of a given words found in hot posts of a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    hder = {'User-Agent': 'User-Agent 2.0'}
    word_list = [i.lower() for i in word_list]
    if not instances:
        instances = [0] * len(word_list)

    if after:
        url += f"?after={after}"

    resp = requests.get(url, headers=hder, allow_redirects=False)

    if resp:
        for i in resp.json().get('data', {}).get('children', []):
            title = [j.lower() for j in i['data']['title'].split()]
            for k, L in enumerate(word_list):
                if L in title:
                    instances[k] += title.count(L)
        after_page = resp.json().get('data', {}).get('after')
        if after_page:
            count_words(subreddit, word_list, instances, after_page)
        else:
            word_dict = {}
            for L in word_list:
                k = word_list.index(L)
                if instances[k] != 0:
                    word_dict[L] = instances[k] * word_list.count(L)
            for key, value in sorted(
                    word_dict.items(), key=lambda x: (-x[1], x[0])):
                print(f"{key}: {value}")
