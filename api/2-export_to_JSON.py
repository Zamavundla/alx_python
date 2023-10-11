#!/ usr/bin/python3

import requests
import json

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data['id']
    user_name = user_data['name']

    # Get employee's TODO list
    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Create a JSON object for the employee's tasks
    employee_tasks = []
    for task in todo_data:
        completed_status = "Completed" if task['completed'] else "Incomplete"
        employee_tasks.append({
            "task": task['title'],
            "completed": completed_status,
            "username": user_name
        })

    # Create a JSON file for the employee
    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump({user_id: employee_tasks}, json_file, indent=2)

    print(f"Employee {user_name}'s tasks have been exported to {json_filename} in JSON format.")  # noqa: E501

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
