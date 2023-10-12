#!/ usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data['name']

    # Get employee's TODO list
    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Calculate the progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    # Print the progress in the requested format
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
