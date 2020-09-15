#!/usr/bin/python3

""" 0-gather_data_from_an_API module

    Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress.

"""

if __name__ == "__main__":

    import json
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
    my_dict = {employee_id: []}
    for a_todo in todos:
        if a_todo.get("userId") == int(employee_id):
            task = {'task': a_todo.get('title'),
                    'completed': a_todo.get('completed'),
                    'username': user.get('username')}
            my_dict.get(employee_id).append(task)

    with open('{}.json'.format(employee_id), 'w') as f:
        json.dump(my_dict, f)
