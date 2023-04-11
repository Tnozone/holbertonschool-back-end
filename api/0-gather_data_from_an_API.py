#!/usr/bin/python3
"""returns information about TODO list progress"""

import requests
from sys import argv


if __name__ == "__main__":
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data_todos = r_todos.json()

    r_users = requests.get('https://jsonplaceholder.typicode.com/users/')
    data_users = r_users.json()

    for i in data_todos:
        if i.get("userId") == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if i.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(i.get("title"))

    for i in data_users:
        if i.get("id") == int(argv[1]):
            employee = i.get("name")

    print("Employee {} is done with tasks({}/{}):".format(
        employee, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for titles in TASK_TITLE:
        print("\t {}".format(titles))
