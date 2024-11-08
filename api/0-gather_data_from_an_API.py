#!/usr/bin/python3
"""
This script fetches and displays employee TODO list progress from an API.
"""
import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetches employee data from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def display_progress(employee_data):
    """Displays the employee's TODO list progress."""
    completed_tasks = [task['title'] for\
        task in employee_data if task['completed']]
    total_tasks = len(employee_data)
    employee_name = employee_data[0].get('username')
    print(f"Employee {employee_name}is done with tasks({len\
        (completed_tasks)}/{total_tasks}):")
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
    display_progress(employee_data)
