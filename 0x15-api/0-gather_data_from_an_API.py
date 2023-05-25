#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    tasks = requests.get("{}users/{}/todos".format(url, sys.argv[1])).json()
    c_tasks = [task for task in tasks if task.get("completed") is True]
    titles = [task.get("title") for task in tasks
              if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name.get("name"), len(c_tasks), len(tasks)))
    for title in titles:
        print("\t {}".format(title))
