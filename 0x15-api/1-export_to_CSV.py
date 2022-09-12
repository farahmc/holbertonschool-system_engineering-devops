#!/usr/bin/python3
""" export data in CSV format"""

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
