#!/usr/bin/python3
"""
A module that gets data from an api
"""
from json import dump
import requests


if __name__ == '__main__':

    def employee_info(arg1, arg2=None):
        """
        Returns information about an employee's TODOLIST
        """
        # Gets the url of the api
        url = 'https://jsonplaceholder.typicode.com/'

        # Adds the command line argument
        url += arg1

        # Checks arguments is present or not
        if arg2:
            url += ('?' + arg2[0] + '=' + arg2[1])

        # Gets the url
        req = requests.get(url)
        # converts to json file
        req = req.json()
        return (req)

    to_jsn = {}

    users = employee_info('users')
    for i in users:
        u_id = i['id']
        to_jsn.update({u_id: []})
        user_task = employee_info('todos', ('userId', str(u_id)))
        for task in user_task:
            to_jsn[u_id].append(
                    {'username': i['username'], 'task': task['title'],
                        'completed': task['completed']}
                    )
    file_ = 'todo_all_employees.json'
    with open(file_, 'w') as f:
        dump(to_jsn, f)
