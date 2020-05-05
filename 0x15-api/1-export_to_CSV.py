#!/usr/bin/python3
""" Extend the first Python script to export data in the CSV format. """
import requests
import csv
from sys import argv


if __name__ == '__main__':
    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(argv[1]))
    username = req.json().get('username')
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(argv[1]))
    data = req.json()
    done = 0
    total = 0

    with open('{}.csv'.format(argv[1]), mode='w') as data_file:
        csv_writer = csv.writer(data_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in data:
            csv_writer.writerow([argv[1], username, task.get('completed'),
                                 task.get('title')])
