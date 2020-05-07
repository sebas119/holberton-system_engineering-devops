#!/usr/bin/python3

"""Reddit Api calls module"""

import requests


def number_of_subscribers(subreddit):
    """Get total number of subscribers of a subreddit"""

    headers = {'User-Agent': 'python3:holberton.task:v1.0 (by /u/sebas119_)'}
    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers, allow_redirects=False)

    if response.status_code == 404 or response.status_code == 302:
        return 0

    return response.json().get('data').get('subscribers')
