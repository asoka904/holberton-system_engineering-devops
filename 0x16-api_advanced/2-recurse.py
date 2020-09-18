#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ recursively """
    if after is None:
        return []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'python3'}
    params = {'limit': 100, 'after': after}
    res = requests.get(url=url, headers=headers, params=params)
    if res.status_code == 404:
        return None

    res = res.json()
    for post in res.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    after = res.get('data').get('after')
    return recurse(subreddit, hot_list, after)
