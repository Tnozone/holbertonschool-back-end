#!/usr/bin/python3
""" Records all tasks from all employees """

import json
import requests


if __name__ == "__main__":
    g_url = "https://jsonplaceholder.typicode.com/"
    first_url = requests.get(g_url + "users").json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            data.get("id"): [{
                "username": data.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")}
                for todo in requests.get(
                    g_url + "todos", params={"userId": data.get("id")}).json()]
                for data in first_url}, file)
