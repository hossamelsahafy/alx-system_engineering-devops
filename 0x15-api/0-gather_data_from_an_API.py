#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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

    Total_Todos = len(Todos)
    Completed_Todos = len([Todo for Todo in Todos if Todo['completed']])

    print("Employee {} is done with tasks({}/{}):"
          .format(User['name'], Completed_Todos, Total_Todos))

    for Todo in Todos:
        if Todo['completed']:
            print("\t {}".format(Todo['title']))


Employee_Id = sys.argv[1]
Todo_Pro(Employee_Id)
