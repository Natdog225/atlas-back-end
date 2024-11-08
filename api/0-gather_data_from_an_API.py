#!/usr/bin/python3
"""
This script retrieves and displays an employee's TODO list
progress using the JSONPlaceholder API.
"""

import json  # Import json module
import sys

import requests


def fetch_employee_data(employee_id):
    """Fetches employee data from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def display_progress(employee_id, employee_data):
    """
    Displays the employee's TODO list progress.

    Fetches the employee's username and calculates their task
    completion progress, displaying the results in a specific format.
    """
    total_tasks = len(employee_data)
    done_tasks = [task for task in employee_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Fetch username separately (since it's not in the task data)
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    # Error handling for API request
    if user_response.status_code != 200:
        print("Employee not found")
        return
    employee_name = user_response.json().get("name")

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")  # Using get() for safety


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            employee_data = fetch_employee_data(employee_id)
            display_progress(employee_id, employee_data)
        except ValueError:
            print("Employee ID must be an integer.")