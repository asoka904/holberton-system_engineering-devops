#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit.
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ Get request obtain suscribers """
    headers = {'User-Agent': 'python3'}

    response = requests.get('https://www.reddit.com/r/{}/about'.
                            format(subreddit), headers=headers)

    if response.status_code != 200:
        return 0

    response = requests.get('https://www.reddit.com/r/{}/about.json'.
                            format(subreddit), headers=headers).json()

    return response.get('data').get('subscribers')
