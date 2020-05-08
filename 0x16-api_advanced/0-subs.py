#!/usr/bin/python3
""" Returns the number of subscribers (not active users, total subscribers)
for a given subreddit. """
import json
import requests


def number_of_subscribers(subreddit):
    """ get request obtain suscribers """
    headers = {'User-Agent': 'python3'}

    response = requests.get('https://www.reddit.com/r/{}/about'.
                            format(subreddit), headers=headers)

    if response.status_code != 200:
        return 0

    n_response = requests.get('https://www.reddit.com/r/{}/about.json'.
                              format(subreddit), headers=headers).json()

    return n_response.get('data').get('subscribers')
