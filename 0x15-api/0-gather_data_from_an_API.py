#!/usr/bin/python3

"""Gather data from an API and return information
about his/her TODO list progress."""

if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    req_user_todo = requests.get("{}/users/{}/todos".format(base_url, user_id))
    req_user_info = requests.get("{}/users/{}".format(base_url, user_id))

    data_user_todo = req_user_todo.json()
    data_user_info = req_user_info.json()

    todo_title = []
    total_task = 0
    todo_task = 0
    for todo in data_user_todo:
        if todo.get("completed") is True:
            todo_task += 1
            todo_title.append(todo.get("title"))
        total_task += 1

    print("Employee {} is done with tasks({}/{}):".format(
        data_user_info.get("name"), todo_task, total_task))
    [print("\t {}".format(todo)) for todo in todo_title]
