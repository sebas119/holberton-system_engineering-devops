#!/usr/bin/python3

"""Reddit Api calls module"""

import requests


def recurse(subreddit, after='', hot_list=[]):
    """Returns a list containing the titles of
    all hot articles for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python3:holberton.task:v1.0 (by /u/sebas119_)'}
    payload = {'limit': '100', 'after': after}
    response = requests.get(url, headers=headers,
                            params=payload, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, after, hot_list)
        return hot_list
    else:
        return None
