#!/usr/bin/python3
""" Write a Python script that returns information about a given employee's
 TODO list progress using a REST API. The script must accept an integer as
 a parameter, which is the employee ID """

from sys import argv
from requests import get

if __name__ == "__main__":
    id = argv[1]
    r_employee = get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(id))
    employee = r_employee.json()

    r_todo = get('https://jsonplaceholder.typicode.com/todos/?userId={}'.
                 format(id))
    todo = r_todo.json()

    todo_total = 0
    todo_complete = 0
    todo_complete_list = []
    for task in todo:
        todo_total += 1
        if task['completed'] is True:
            todo_complete += 1
            todo_complete_list.append(task['title'])

    print("Employee {} is done with tasks({}/{}):".
          format(employee['name'], todo_complete, todo_total))
    for task in todo_complete_list:
        print("\t {}".format(task))
