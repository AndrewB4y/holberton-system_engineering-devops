#!/usr/bin/python3

""" 1-top_ten module """
import json
import requests


def top_ten(subreddit):
    """ top_ten function
    Quieries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;'
               ' Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/85.0.4183.102 Safari/537.36'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    r = r.json()
    if 'error' not in r:
        r = r.get('data').get('children')
        for idx, post in enumerate(r):
            if idx == 10:
                return
            print(post.get('data').get('title'))
    else:
        print('None')
