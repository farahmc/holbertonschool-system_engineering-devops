#!/usr/bin/python3
""" export all employees in JSON format"""

import json
from requests import get
from sys import argv

if __name__ == "__main__":
    r_employee = get('https://jsonplaceholder.typicode.com/users/')
    employee = r_employee.json()

    employee_dict = {}
    for e in employee:
        todo_list = []
        id = e['id']
        r_todo = get("https://jsonplaceholder.typicode.com/todos/?userId={}".
                     format(id))
        todo = r_todo.json()
        for task in todo:
            todo_dict = {}
            todo_dict["username"] = e['username']
            todo_dict["task"] = task['title']
            todo_dict["completed"] = task['completed']
            todo_list.append(todo_dict)
        employee_dict[id] = todo_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(employee_dict, json_file)
