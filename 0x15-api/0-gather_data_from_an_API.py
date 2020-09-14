#!/usr/bin/python3

""" 0-gather_data_from_an_API module

    Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress.

"""

if __name__ == "__main__":

    import requests
    import sys

    v = sys.argv
    employee_id = v[1]
    req_users = 'https://jsonplaceholder.typicode.com/users/{}'
    req_todos = 'https://jsonplaceholder.typicode.com/todos'
    r_us = requests.get(req_users.format(employee_id))
    r_todos = requests.get(req_todos)

    try:
        user = r_us.json()
        todos = r_todos.json()
        if user == {} or todos == {}:
            print("No result")
        else:
            my_dict = {}
            my_dict.update({'name': user['name']})
            done_td = 0
            total_td = 0
            titles = []
            for a_todo in todos:
                if a_todo["userId"] == int(employee_id):
                    total_td += 1
                    if a_todo['completed'] is True:
                        done_td += 1
                        titles.append(a_todo['title'])
            ts = "\n\t".join(titles)
            my_dict.update({'t_td': total_td,
                            'd_td': done_td,
                            'ts': ts})
            m = "Employee {name} is done with tasks({d_td}/{t_td}):\n\t{ts}"
            print(m.format(**my_dict))
    except Exception as error:
        print(error)
