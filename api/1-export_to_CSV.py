#!/usr/bin/python3
"""This code checks the student's IDs if they are in the CSV file and in alphabetic order"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"

def check_csv(employee_id):
    # Get the list of TODOs
    todos_url = f"{todos_url}?userId={employee_id}"
    todo_response = requests.get(todos_url)
    todo_data = todo_response.json()

    # Create a CSV file for the employee
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Get employee details
        user_url = f"{users_url}{employee_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()
        user_id = user_data[0]['id']
        user_name = user_data[0]['username']

        for task in todo_data:
            completed_status = "True" if task['completed'] else "False"
            csv_writer.writerow(user_id, user_name, completed_status, task['title'])

    # Check the number of tasks in the CSV
    num_tasks_in_csv = len(todo_data)
    with open(csv_filename, 'r') as csv_file:
        num_lines = sum(1 for _ in csv_file)

    # Check user ID and username
    with open(csv_filename, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        csv_header = next(csv_data)
        user_id_col = csv_header.index("USER_ID")
        username_col = csv_header.index("USERNAME")
        for row in csv_data:
            if int(row[user_id_col]) != user_id or row[username_col] != user_name:
                print("User ID and Username: Incorrect")
                break
        else:
            print("User ID and Username: OK")

    # Check CSV formatting
    with open(csv_filename, 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        for i, row in enumerate(csv_data, start=1):
            if len(row) != 4 or not row[0].isdigit() or not (row[2] == "True" or row[2] == "False"):
                print(f"Task {i} Formatting: Incorrect")
                break
        else:
            print("Formatting: OK")

    # Print the number of tasks in CSV
    print(f"Number of tasks in CSV: {'OK' if num_tasks_in_csv == num_lines - 1 else 'Incorrect'}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <script_name> <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    check_csv(employee_id)
