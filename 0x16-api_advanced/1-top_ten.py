#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import json
import requests


def top_ten(subreddit):
    """ top ten """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'python3'}
    params = {'limit': 10}
    res = requests.get(url=url, headers=headers, params=params)

    if res.status_code == 404:
        print('None')
        return

    list = res.json().get('data').get('children')
    for post in list:
        print(post.get('data').get('title'))
