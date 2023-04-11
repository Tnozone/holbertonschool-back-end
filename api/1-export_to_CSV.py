#!/usr/bin/python3
"""returns information about TODO list progress"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    rows = []
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data_todos = r_todos.json()

    r_users = requests.get('https://jsonplaceholder.typicode.com/users/')
    data_users = r_users.json()

    for i in data_users:
        if i.get("id") == int(argv[1]):
            employee = i.get("username")

    with open(argv[1] + '.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in data_todos:
            rows = []
            if i.get("userId") == int(argv[1]):
                rows.append(i.get("userId"))
                rows.append(employee)
                rows.append(i.get("completed"))
                rows.append(i.get("title"))
                writer.writerow(rows)
