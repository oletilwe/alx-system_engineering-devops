#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


def fetch_todo_list_progress(employee_id):

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
            )

    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        employee_name = user_response.json()['name']
    else:
        print(f"Failed to fetch data for employee ID: {employee_id}")
        return

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Failed to fetch the TODO list.")
        return

    todos = todos_response.json()

    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    print(
            f"Employee {employee_name} is done with tasks"
            f"({completed_tasks}/{total_tasks}):"
            )
    for todo in todos:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
