#!/ usr/bin/python3

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data['id']
    user_name = user_data['username']

    # Get employee's TODO list
    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Create a CSV file for the employee
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            completed_status = "True" if task['completed'] else "False"
            csv_writer.writerow([user_id, user_name, completed_status, task['title']])

    # Check the number of tasks in the CSV
    num_lines = 0
    with open(csv_filename, 'r') as f:
        for line in f:
            if not line == '\n':
                num_lines += 1

    print(f"Number of tasks in CSV: {'OK' if len(todo_data) == num_lines else 'Incorrect'}")

    # Check user ID and username
    with open(csv_filename, 'r') as f:
        for line in f:
            if not line == '\n':
                if not str(user_id) in line or not str(user_name) in line:
                    print("User ID and Username: Incorrect")
                    break
        else:
            print("User ID and Username: OK")

    # Check CSV formatting
    with open(csv_filename, 'r') as f:
        output = f.read().strip()
        count = 0
        for task in todo_data:
            count += 1
            expected_line = f'"{user_id}","{user_name}","{str(task["completed"])}","{task["title"]}"'
            if not expected_line in output:
                print(f"Task {count} Formatting: Incorrect")
                break
        else:
            print("Formatting: OK")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <script_name> <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
