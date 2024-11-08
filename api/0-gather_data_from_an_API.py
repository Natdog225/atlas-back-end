#!/usr/bin/python3
"""
This script fetches and displays employee TODO list progress from an API.
"""
import csv
import json
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetches employee data from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{1}/todos"
    response = requests.get(url)
    return response.json()


def display_progress(employee_id, employee_data):
    """Displays the employee's TODO list progress.

    Fetches the employee's username and calculates their task
    completion progress, displaying the results in a specific format.
    """
    completed_tasks = [
        task['title'] for task in employee_data if task['completed']
    ]
    total_tasks = len(employee_data)

    # Fetch username separately (since it's not in the task data)
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    employee_name = user_response.json().get('username')

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data = fetch_employee_data(employee_id)
    display_progress(employee_id, employee_data)
