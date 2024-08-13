#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import re
import sys
import requests

def fetch_employee_data(employee_id):
    # URLs for the API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    # Fetch user data
    users_response = requests.get(users_url)
    users = users_response.json()
    
    # Fetch TODO data
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    
    # Find the user with the given employee ID
    user = next((user for user in users if user['id'] == employee_id), None)
    if not user:
        print(f"User with ID {employee_id} not found.")
        return

    # Collect TODOs for the user
    user_todos = [todo for todo in todos if todo['userId'] == employee_id]
    
    # Calculate number of completed and total tasks
    total_tasks = len(user_todos)
    completed_tasks = sum(1 for todo in user_todos if todo['completed'])
    
    # Print employee TODO list progress
    print(f"Employee {user['name']} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Print titles of completed tasks
    for todo in user_todos:
        if todo['completed']:
            print(f"     {todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        fetch_employee_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
