#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

This script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import csv
import requests
import sys


def fetch_todo_list_and_export_to_csv(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user = user_response.json()
        employee_name = user['name']
        username = user['username']
    except requests.HTTPError:
        print(f"Failed to fetch data for employee ID: {employee_id}")
        return

    try:
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()
    except requests.HTTPError:
        print("Failed to fetch the TODO list.")
        return

    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                employee_id,
                username,
                todo['completed'],
                todo['title']
            ])

    print(f"Data for employee {employee_name} has been written to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_and_export_to_csv(employee_id)
