#!/usr/bin/python3
""" export data in JSON format"""

import json
from requests import get
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    r_employee = get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(id))
    employee = r_employee.json()

    r_todo = get('https://jsonplaceholder.typicode.com/todos/?userId={}'.
                 format(id))
    todo = r_todo.json()
    json_filename = id + ".json"

    todo_dict = {}
    todo_list = []
    for task in todo:
        todo_dict["task"] = task['title']
        todo_dict["completed"] = task['completed']
        todo_dict["username"] = employee['username']
        todo_list.append(todo_dict)

    user_todo_dict = {}
    user_todo_dict[id] = todo_list

    with open(json_filename, "w") as json_file:
        json.dump(user_todo_dict, json_file)
