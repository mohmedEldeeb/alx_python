#!/usr/bin/python3

import csv
import requests
import sys


employee_id = int(sys.argv[1])


def main():
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data['name']

        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for task in todo_data:
                task_completed_status = "True" if task['completed'] else "False"
                task_title = task['title']
                csv_writer.writerow([employee_id, employee_name, task_completed_status, task_title])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Error: User with ID {employee_id} not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(" Usage:  CSV.py USER_ID")
        sys.exit(1)

    main()