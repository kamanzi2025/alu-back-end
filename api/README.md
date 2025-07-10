# API Directory Documentation

This directory contains Python scripts for interacting with a REST API
(specifically, JSONPlaceholder) to retrieve and export employee data.

## Scripts

### `0-gather_data_from_an_API.py`
*(Assuming this is your first script from Task 0)*
This script is designed to fetch information for a specific employee, including their details and their list of TODO tasks, from the JSONPlaceholder API. It takes an employee ID as a command-line argument.

### `1-export_to_CSV.py`
This script extends the functionality of `0-gather_data_from_an_API.py` by exporting the retrieved employee and task data into a CSV file.
- **Usage:** `python3 1-export_to_CSV.py <employee_id>`
- **Output:** A CSV file named `<employee_id>.csv` will be created in this directory.
- **Format:** Each row in the CSV will be formatted as `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`.

### `2-export_to_JSON.py`
This script also extends the functionality to export employee and task data, but in JSON format.
- **Usage:** `python3 2-export_to_JSON.py <employee_id>`
- **Output:** A JSON file named `<employee_id>.json` will be created in this directory.
- **Format:** The JSON structure will be `{"USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...]}`.

## How to Use

1.  **Navigate to the `api` directory:**
    ```bash
    cd alu-back-end/api
    ```
2.  **Run the desired script with an employee ID:**
    ```bash
    python3 1-export_to_CSV.py 2
    # or
    python3 2-export_to_JSON.py 5
    ```
3.  **View the generated file:**
    ```bash
    cat 2.csv
    # or
    cat 5.json
    ```

## Dependencies

These scripts require the `requests` library to make HTTP requests to the API. If you encounter issues, ensure it's installed:
```bash
pip install requests
# or for Python 3 specific install
pip3 install requests
