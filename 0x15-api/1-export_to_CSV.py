#!/usr/bin/python3
"""
    Using this REST API (https://jsonplaceholder.typicode.com/), for a given
    employee ID, returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    name = req.json().get('username')
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data = req.json()

    with open('{}.csv'.format(argv[1]), mode='w') as data_file:
        csv_writer = csv.writer(data_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)

    for task in data:
        csv_writer.writerow([argv[1], username, task.get('completed'),
                            task.get('title')])
