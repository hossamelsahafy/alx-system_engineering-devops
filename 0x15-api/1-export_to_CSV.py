#!/usr/bin/python3
"""
script to export data in the CSV format.
"""
import requests
import sys
import csv
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

    with open("{}.csv".format(ID), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for Todo in Todos:
            writer.writerow([ID, User.get('username'), Todo.get('completed'),
                            Todo.get('title')])


if __name__ == "__main__":
    Employee_Id = sys.argv[1]
    Todo_Pro(Employee_Id)
