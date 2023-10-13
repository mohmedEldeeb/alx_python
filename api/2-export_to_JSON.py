import json
import requests

def getEmployeeAndTodo(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    res = requests.get(url)
    todos = res.json()

    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    res = requests.get(url)
    employee = res.json()

    completed_tasks = len([todo for todo in todos if todo['completed']])
    all_tasks = len(todos)

    # Print progress report
    print(f"Employee {employee['name']} is done with tasks({completed_tasks}/{all_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f'\t{todo["title"]}')

    data = {str(id): []}
    for todo in todos:
        data[str(id)].append({
            'task': todo['title'],
            'completed': todo['completed'],
            'username': employee['name']
        })

    with open(f'{id}.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
        