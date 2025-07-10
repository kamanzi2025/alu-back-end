#!/usr/bin/python3
"""
This script fetches an employee's TODO list and user details from a REST API
(JSONPlaceholder) and exports the data into a CSV file.
The script takes an employee ID as a command-line argument.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports tasks owned by a specific employee to a CSV file.

    It fetches user information and their associated TODO tasks from the
    JSONPlaceholder API. The data is then written to a CSV file named
    <employee_id>.csv, with each record formatted as:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

    Args:
        employee_id (int): The ID of the employee whose tasks are to be exported.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_url = f"{base_url}/users/{employee_id}"
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
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

    username = user_data.get("username")
    if username is None: # Added a check for username existence
        print(f"Error: Username not found for user ID {employee_id}.")
        sys.exit(1)

    # Fetch user's TODO list
    todos_url = f"{base_url}/todos"
    try:
        todos_response = requests.get(todos_url, params={"userId": employee_id})
        todos_response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        todos_data = todos_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODOs data: {e}")
        sys.exit(1)
    except ValueError:
        print("Error: Could not decode JSON response for TODOs data.")
        sys.exit(1)

    # Define the CSV file name
    csv_ 
   
