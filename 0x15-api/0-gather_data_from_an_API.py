#!/usr/bin/python3
""" Write a Python script that returns information about a given employee's TODO list progress using a REST API.
  The script must accept an integer as a parameter, which is the employee ID """

from sys import argv
from requests import get

if __name__ == "__main__":
    r_user = get('https://jsonplaceholder.typicode.com/users/')
    print(r_user.text)