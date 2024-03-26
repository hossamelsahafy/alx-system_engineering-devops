#!/usr/bin/python3
"""
script to export data in the JSON format.
"""
import json
import requests
import sys


def Todo_Pro(ID):
    """
    Getting Details From WebSite
    """
    U_RES = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(ID))
    User = U_RES.json()

    Base_Url = "https://jsonplaceholder.typicode.com/users/"
    Todos_Endpoint = "{}/todos".format(ID)
    T_RES = requests.get(Base_Url + Todos_Endpoint)
    Todos = T_RES.json()

    data = []
    for Todo in Todos:
        if Todo.get('userId') == int(ID):
            data.append({
                "task": Todo.get('title'),
                "completed": Todo.get('completed'),
                "username": User.get('username')
            })

    with open("{}.json".format(ID), "w") as json_file:
        json.dump({ID: data}, json_file)


if __name__ == "__main__":
    Employee_Id = sys.argv[1]
    Todo_Pro(Employee_Id)
