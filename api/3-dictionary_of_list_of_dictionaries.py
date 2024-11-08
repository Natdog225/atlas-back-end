#!/usr/bin/python3
"""
This script retrieves the TODO list progress for all employees and
exports the data to a JSON file in a specific format.
"""

import json

import requests


def fetch_employee_data(employee_id):
    """Fetches employee data from the API."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()


def fetch_all_employees_data():
    """Fetches and formats TODO list data for all employees."""
    all_employees_data = {}
    for employee_id in range(1, 11):  # Assuming employee IDs from 1 to 10
        employee_data = fetch_employee_data(employee_id)

        # Fetch username
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)
        username = user_response.json().get("username")

        # Format data for JSON
        tasks = []
        for task in employee_data:
            tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        all_employees_data[str(employee_id)] = tasks

    return all_employees_data


if __name__ == "__main__":
    all_employees_data = fetch_all_employees_data()

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_employees_data, jsonfile)
