#!/usr/bin/python3

"""Reddit Api calls module"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed
    for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python3:holberton.task:v1.0 (by /u/sebas119_)'}
    payload = {'limit': '10'}
    response = requests.get(url, headers=headers,
                            params=payload, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print("None")
