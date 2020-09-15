#!/usr/bin/python3

""" 1-export_to_CSV

    Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress.

    After this, it'll export to a csv file.

"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    v = sys.argv
    employee_id = v[1]
    req_users = 'https://jsonplaceholder.typicode.com/users/{}'
    req_todos = 'https://jsonplaceholder.typicode.com/todos'
    r_us = requests.get(req_users.format(employee_id))
    r_todos = requests.get(req_todos)
    user = r_us.json()
    todos = r_todos.json()
    my_dict = {}
    content = []
    fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    for a_todo in todos:
        if a_todo.get("userId") == int(employee_id):
            content.append({"USER_ID": str(a_todo.get('userId')),
                            "USERNAME": str(user.get('username')),
                            "TASK_COMPLETED_STATUS":
                            str(a_todo.get('completed')),
                            "TASK_TITLE": str(a_todo.get('title'))})

    with open('{}.csv'.format(employee_id), 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=fields,
                                quoting=csv.QUOTE_ALL)
        for data in content:
            writer.writerow(data)
