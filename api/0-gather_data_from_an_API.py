#!/usr/bin/python3
"""
This script fetches an employee's TODO list and user details from a REST API
(JSONPlaceholder) and displays their progress.
The script takes an employee ID as a command-line argument.
"""
import requests
import sys

def gather_data_from_an_API(employee_id):
    """
    Fetches and displays the progress of a given employee's TODO list.

    It retrieves user information and their associated TODO tasks from the
    JSONPlaceholder API, then prints a summary of completed tasks.

    Args:
        employee_id (int): The ID of the employee whose data is to be gathered.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_url = f"{base_url}/users/{employee_id}"
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise HTTPError for bad responses
        user_data = user_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        sys.exit(1)
    except ValueError:
        print("Error: Could not decode JSON response for user data.")
        sys.exit(1)

    if not user_data:
        print(f"Error: No user found with ID {employee_id}")
        return

    employee_name = user_data.get("name")
    if employee_name is None:
        print(f"Error: Employee name not found for user ID {employee_id}.")
        sys.exit(1)

    # Fetch user's TODO list (likely the source of line 22 and 23 errors)
    todos_url = f"{base_url}/todos"
    try:
        todos_response = requests.get(todos_url, params={"userId": employee_id})
        todos_response.raise_for_status()  # Raise HTTPError for bad responses
        todos_data = todos_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODOs data: {e}")
        sys.exit(1)
    except ValueError:
        print("Error: Could not decode JSON response for TODOs data.")
        sys.exit(1)

    # Calculate completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)

    # Print summary (likely the source of line 32 error)
    # The original line 32 was likely too long. This breaks it to fit PEP8.
    print(f"Employee {employee_name} is in progress with tasks"
          f"({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        # Indent with tabs, but PEP8 prefers 4 spaces. Assuming original used 4 spaces.
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_data_from_an_API(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1) 

