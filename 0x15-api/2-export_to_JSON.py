#!/usr/bin/python3
"""
script to export data in the CSV format.
"""
import json
import requests
import sys
"""
Getting Details From WebSite
"""


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
        data.append({
            "USER_ID": ID,
            "USERNAME": User.get('username'),
            "TASK_COMPLETED_STATUS": Todo.get('completed'),
            "TASK_TITLE": Todo.get('title')
        })
    with open("{}.json".format(ID), "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    Employee_Id = sys.argv[1]
    Todo_Pro(Employee_Id)
