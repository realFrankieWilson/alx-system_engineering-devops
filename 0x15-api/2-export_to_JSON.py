#!/usr/bin/python3
"""
A module that gets data from an api
"""
from json import dump
import requests
import sys


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

    # Gets the specific data from the command line
    user_ = employee_info('users', ('id', sys.argv[1]))[0]
    tasks_ = employee_info('todos', ('userId', sys.argv[1]))

    # Current format
    user_id = user_['id']
    to_jsn = {user_id: []}
    for task in tasks_:
        to_jsn[user_id].append(
                {'task': task['title'], 'completed': task['completed'],
                    'username': user_['username']}
                )
    file_ = sys.argv[1] + '.json'
    with open(file_, 'w') as f:
        dump(to_jsn, f)
