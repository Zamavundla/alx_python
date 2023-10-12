#!/ usr/bin/python3

import requests
import json
import sys

def export_employee_todo_to_json(employee_id):
    # Define the base URLs for the API
    users_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId="

    # Get employee details
    user_response = requests.get(users_url + str(employee_id))
    user_data = user_response.json()

    if not user_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    user_name = user_data[0]['username']

    # Get employee's TODO list
    todo_response = requests.get(todos_url + str(employee_id))
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
