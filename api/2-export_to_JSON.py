#!/usr/bin/python3

import requests
import json
import sys

"""This module provides functions to export an employee's TODO tasks to a JSON file."""

def export_employee_todo_to_json(employee_id):
    """
    Export an employee's TODO tasks to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None

    Raises:
        ValueError: If the `employee_id` is not a valid integer.
    """

    # Define the base URLs for the API
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Rest of your code...
    # Get employee details
    user_response = requests.get(users_url)
    user_data = user_response.json()

    if not user_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    user_name = user_data['username']

    # Get employee's TODO list
    todo_response = requests.get(todos_url)
    todo_data = todo_response.json()

    # Create a JSON object for the employee's tasks
    employee_tasks = []
    for task in todo_data:
        completed_status = task['completed']
        employee_tasks.append({
            "task": task['title'],
            "completed": completed_status,
            "username": user_name
        })

    # Create a JSON file for the employee
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump({str(employee_id): employee_tasks}, json_file, indent=2)

    print(f"Employee {user_name}'s tasks have been exported to {json_filename} in JSON format.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_employee_todo_to_json(employee_id)
        except ValueError:
            print("Employee ID must be an integer.")
