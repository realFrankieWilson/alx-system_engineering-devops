#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, instances={}, after=None, count=0):
    """
    Counts and print of a given words found in hot posts of a given subreddit
    """
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    head = {'User-Agent': 'User-Agent 2.0'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    resp = requests.get(
        api_url, headers=head, params=params, allow_redirects=False
        )

    try:
        result = resp.json()
        if resp.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    result = result.get('data')
    after = result.get('after')
    count += result.get('dist')

    for info in result.get('children'):
        title = info.get('data').get('title').lower().split()
        for wrd in word_list:
            if wrd.lower() in title:
                times = len([tm for tm in title if tm == wrd.lower()])
                if instances.get(wrd) is None:
                    instances[wrd] = times
                else:
                    instances[wrd] += times

    if after is None:
        if len(instances) == 0:
            print('')
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print('{}: {}'.format(k, v)) for k, v, in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
