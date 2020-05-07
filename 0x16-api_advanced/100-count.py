#!/usr/bin/python3

"""Reddit Api calls module"""

import requests


def count_words(subreddit, word_list, after='', words_counting={}):
    """parses the title of all hot articles, and prints
    a sorted count of given keywords"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python3:holberton.task:v1.0 (by /u/sebas119_)'}
    payload = {'limit': '100', 'after': after}
    response = requests.get(url, headers=headers,
                            params=payload, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children_list = data.get('children')

        for child in children_list:
            title = child.get('data').get('title')
            for word in word_list:
                ocurrences = title.lower().split().count(word.lower())
                if ocurrences > 0:
                    if word in words_counting:
                        words_counting[word] += ocurrences
                    else:
                        words_counting[word] = ocurrences

        if after is not None:
            return count_words(subreddit, word_list, after, words_counting)
        else:
            if len(words_counting) > 0:
                iterator = sorted(words_counting.items(),
                                  key=lambda kv: (-kv[1], kv[0]))
                for key, value in iterator:
                    print('{}: {}'.format(key, value))
            else:
                return
    else:
        return
