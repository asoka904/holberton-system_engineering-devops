#!/usr/bin/python3
"""
    Using this REST API (https://jsonplaceholder.typicode.com/), for a given
    employee ID, returns information about his/her TODO list progress.
"""
import json
import requests
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
        json.dump(out, my_file)
