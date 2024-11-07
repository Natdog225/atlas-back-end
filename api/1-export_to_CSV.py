#!/usr/bin/python3
"""
This script fetches employee TODO list progress and exports it to CSV.
"""
import csv
import sys
import requests


def fetch_employee_data(employee_id):
    """Fetches employee data from the API, including username."""
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    todos_response = requests.get(todos_url)
    user_response = requests.get(user_url)

    return user_response.json().get('username'), todos_response.json()


def display_progress(employee_data):
    """Displays the employee's TODO list progress."""
    completed_tasks = [task['title'] for task in employee_data if task['completed']]
    total_tasks = len(employee_data)
    employee_name = employee_data[0].get('username')
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")


def write_to_csv(employee_id, username, employee_data):
    """Writes employee task data to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in employee_data:
            writer.writerow([employee_id, username, task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    username, employee_data = fetch_employee_data(employee_id)
    display_progress(employee_data)
    write_to_csv(employee_id, username, employee_data)
