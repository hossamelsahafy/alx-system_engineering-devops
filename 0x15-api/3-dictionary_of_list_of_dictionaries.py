#!/usr/bin/python3
"""
script to export data in the JSON format.
"""
import json
import requests


def Todo_Pro():
    """
    Getting Details From WebSite
    """
    U_RES = requests.get("https://jsonplaceholder.typicode.com/users")
    Users = U_RES.json()

    T_RES = requests.get("https://jsonplaceholder.typicode.com/todos")
    Todos = T_RES.json()

    data = {}
    for User in Users:
        ID = User.get('id')
        data[ID] = []
        for Todo in Todos:
            if Todo.get('userId') == ID:
                data[ID].append({
                    "username": User.get('username'),
                    "task": Todo.get('title'),
                    "completed": Todo.get('completed')
                })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    Todo_Pro()
