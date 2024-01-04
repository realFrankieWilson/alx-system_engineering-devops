#!/usr/bin/python3
"""
A module that gets data from an api
"""
import json
import requests
import sys


if __name__ == '__main__':

    def employee_info(arg1, arg2=None):
        """
        Returns information about an employee's TODOLIST
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += arg1
        if arg2:
            url += ('?' + arg2[0] + '=' + arg2[1])
        req = requests.get(url)
        req = req.json()
        return (req)

    user_ = employee_info('users', ('id', sys.argv[1]))
    tasks_ = employee_info('todos', ('userId', sys.argv[1]))
    completed = [i for i in tasks_ if i['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(
        user_[0]['name'], len(completed), len(tasks_))
        )

    for task in completed:
        print('\t {}'.format(task['title']))
