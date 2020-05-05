#!/usr/bin/python3
""" Using this REST API, for a given employee ID, returns information about
his/her TODO list progress. """
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    name = req.json().get('name')
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))

    data = req.json()
    done = 0
    total = 0
    for task in data:
        total += 1
        if task.get('completed'):
            done += 1
    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))

    for task in data:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
