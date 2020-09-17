#!/usr/bin/python3

""" 2-recurse module """

import requests


def recurse(subreddit, hot_list=[], after=''):
    """ recurse function
    queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    """
    if after is None:
        return hot_list

    if after == '':
        url = 'https://www.reddit.com/r/{}/hot.json'
        url = url.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'
        url = url.format(subreddit, after)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/85.0.4183.102 Safari/537.36'}

    r = requests.get(url, headers=headers, allow_redirects=False)
    r = r.json()
    if 'error' not in r:
        r = r.get('data')
        after = r.get('after')
        r = r.get('children')
        hot_list.extend([post.get('title') for post in r])
        recurse(subreddit, hot_list, after)
    else:
        return None
    return hot_list
