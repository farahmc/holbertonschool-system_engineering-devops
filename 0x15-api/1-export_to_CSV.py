#!/usr/bin/python3
""" Write a Python script that returns information about a given employee's
 TODO list progress using a REST API. The script must accept an integer as
 a parameter, which is the employee ID """

import csv
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
    csv_filename = id + ".csv"

    with open(csv_filename, mode="w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([task['userId'], employee['username'],
                            task['completed'], task['title']])
