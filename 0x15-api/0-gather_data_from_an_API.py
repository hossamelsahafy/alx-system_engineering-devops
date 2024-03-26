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
    U_RES = requests.get(f"https://jsonplaceholder.typicode.com/users/{ID}")
    User = U_RES.json()

    T_RES = requests.get(f"https://jsonplaceholder.typicode.com/users/{ID}/todos")
    Todos = T_RES.json()

    Total_Todos = len(Todos)
    Completed_Todos = len([Todo for Todo in Todos if Todo['completed']])

    print(f"Employee {User['name']} is done with tasks ({Completed_Todos}/{Total_Todos}):")

    for Todo in Todos:
        if Todo['completed']:
            print(f"\t {Todo['title']}")


Employee_Id = sys.argv[1]
Todo_Pro(Employee_Id)
