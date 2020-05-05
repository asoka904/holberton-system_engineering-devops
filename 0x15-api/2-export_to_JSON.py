#!/usr/bin/python3
""" Extend the first Python script to export data in the JSON format. """
import requests
import json
from sys import argv

if __name__ == '__main__':
    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    username = req.json().get('username')
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data = req.json()

    out = {}
    out['{}'.format(argv[1])] = []

    for task in data:
        out['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username})
    with open('{}.json'.format(argv[1]), 'w') as my_file:
        json.dump(out, file)
