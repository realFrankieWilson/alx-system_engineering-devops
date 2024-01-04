#!/usr/bin/python3
"""
A module that gets data from an api
"""
import csv
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

    user_ = employee_info('users', ('id', sys.argv[1]))[0]
    tasks_ = employee_info('todos', ('userId', sys.argv[1]))

    cvs_ = sys.argv[1] + '.csv'
    with open(cvs_, 'w') as f:
        file_ = csv.writer(
                f,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_ALL
                )

        for i in tasks_:
            file_.writerow([user_['id'],
                           user_['username'],
                           i['completed'],
                           i['title']])
