#!/usr/bin/python3
""" Extend the first Python script to export data in the JSON format. """
import requests
import json
from sys import argv

if __name__ == '__main__':
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = req.json()

    set_id = set()
    for user in data:
        set_id.add(user.get('userId'))

    out = {}
    for user in set_id:
        req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                           format(user))
        username = req.json().get('username')

        req = requests.get('https://jsonplaceholder.typicode.com/' +
                           'todos?userId={}'.format(user))
        data = req.json()

        out['{}'.format(user)] = []
        for task in data:
            out['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username})

    with open('todo_all_employees.json', 'w') as my_file:
        json.dump({int(x): out[x] for x in out.keys()},
                  my_file, sort_keys=True)
