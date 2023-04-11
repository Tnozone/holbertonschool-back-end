#!/usr/bin/python3
"""returns information about TODO list progress"""

import requests
import sys


if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos_data = todos.json()
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = users.json()
    employee_name = ""

    for data in users_data:
        if int(argv[1]) == data.get("id"):
            employee_name = data.get("name")

    completed_tasks = 0
    total_tasks = 0

    for data in todos_data:
        if int(argv[1]) == data.get("userId"):
            if data.get("completed") is True:
                completed_tasks += 1
            if data.get("completed") is True or data.get("completed") is False:
                total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
            .format(employee_name, completed_tasks, total_tasks))

    task_title = ""
    for data in todos_data:
        if int(argv[1]) == data.get("userId"):
            if data.get("completed") is True:
                task_title = data.get("title")
                print("\t {}".format(task_title))
