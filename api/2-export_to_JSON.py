#!/usr/bin/python3
"""
This script retrieves an employee's TODO list progress and
exports the data to a CSV file.
"""

import csv
import json
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetches employee data from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def write_to_json(employee_id, employee_data):
    """Writes employee task data to a JSON file."""
    filename = f"{employee_id}.json"

    # Fetch username
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    username = user_response.json().get("username")

    # Format data for JSON
    tasks = []
    for task in employee_data:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks}  # Use employee_id as string key

    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            employee_data = fetch_employee_data(employee_id)
            write_to_csv(employee_id, employee_data)
        except ValueError:
            print("Employee ID must be an integer.")
