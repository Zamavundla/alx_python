#!/ usr/bin/python3

import csv
import os
import requests

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

    # Create a CSV file for the employee
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            completed_status = "True" if task['completed'] else "False"
            csv_writer.writerow([user_id, user_name, completed_status, task['title'])

    print(f"Employee {user_name}'s tasks have been exported to {csv_filename} in CSV format.")

    # Display the contents of the CSV file using 'cat' command
    if os.path.exists(csv_filename):
        os.system(f"cat {csv_filename}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
