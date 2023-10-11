#!/ usr/bin/python3

import requests
import json

def export_all_employee_tasks():
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Create a dictionary to store all employee tasks
    all_employee_tasks = {}

    # Fetch user data to get a list of employee IDs
    user_response = requests.get(f"{base_url}/users")
    users_data = user_response.json()

    for user_data in users_data:
        user_id = user_data['id']
        user_name = user_data['name']

        # Get employee's TODO list
        todo_response = requests.get(f"{base_url}/users/{user_id}/todos")
        todo_data = todo_response.json()

        # Create a list for the employee's tasks
        employee_tasks = []
        for task in todo_data:
            completed_status = "Completed" if task['completed'] else "Incomplete"
            employee_tasks.append({
                "username": user_name,
                "task": task['title'],
                "completed": completed_status
            })

        # Store the tasks in the dictionary using the user_id as the key
        all_employee_tasks[user_id] = employee_tasks

    # Create a JSON file for all employee tasks
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employee_tasks, json_file, indent=2)

    print(f"All employee tasks have been exported to {json_filename} in JSON format.")

if __name__ == "__main__":
    export_all_employee_tasks()
