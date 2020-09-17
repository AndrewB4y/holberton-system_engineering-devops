#!/usr/bin/python3

""" 0-subs module """

import requests
import json


def number_of_subscribers(subreddit):
    """
    number_of_subsribers
    queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; '
               'x64) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/85.0.4183.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r = r.json()

    if 'error' not in r:
        return r.get('data').get('subscribers')
    return 0
