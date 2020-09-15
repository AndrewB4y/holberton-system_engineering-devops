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
    req_users = 'https://jsonplaceholder.typicode.com/users'
    req_todos = 'https://jsonplaceholder.typicode.com/todos'
    r_us = requests.get(req_users)
    r_todos = requests.get(req_todos)

    all_users = r_us.json()
    todos = r_todos.json()
    my_dict = {}
    for user in all_users:
        for a_todo in todos:
            if a_todo.get('userId') == user.get('id'):
                task = {'task': a_todo.get('title'),
                        'completed': a_todo.get('completed'),
                        'username': user.get('username')}
                if my_dict.get(a_todo.get('userId')) is not None:
                    my_dict.get(a_todo.get('userId')).append(task)
                else:
                    my_dict.update({a_todo.get('userId'): [task]})

    with open('todo_all_employees.json', 'w') as f:
        json.dump(my_dict, f)
