#!/usr/bin/python3

""" 100-count module """

import requests


def count_words(subreddit, word_list, after=''):
    """ count_words function
    Queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords.
    """

    """ Converting word_list to dictionary and setting each count to 0 """
    if type(word_list) is list:
        temp = {}
        temp2 = set([word.lower() for word in word_list])
        for word in word_list:
            if word.lower() in temp2:
                temp.update({word: 0})
                temp2.remove(word.lower())
        word_list = temp

    """ When after is None, means the end of the queries"""
    if after is None:
        temp = [w for w in word_list.items()]
        temp.sort(key=lambda w: (-w[1], w[0]))
        for w in temp:
            if w[1] != 0:
                print("{}: {:d}".format(w[0], w[1]))
        return

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
    if r.status_code == 200:
        r = r.json()
        r = r.get('data')
        after = r.get('after')
        r = r.get('children')
        for post in r:
            check = post.get('data').get('title').lower().split()
            for w in word_list:
                word_list[w] += check.count(w.lower())
        count_words(subreddit, word_list, after)
    else:
        return
