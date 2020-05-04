#!/usr/bin/python3

"""Export to JSON data from the previous task"""

if __name__ == "__main__":
    import requests
    import sys
    import json

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    req_user_todo = requests.get("{}/users/{}/todos".format(base_url, user_id))
    req_user_info = requests.get("{}/users/{}".format(base_url, user_id))

    data_user_todo = req_user_todo.json()
    data_user_info = req_user_info.json()
    username = data_user_info.get("username")

    data = {}
    tasks = []
    for todo in data_user_todo:
        task = {"task": "", "completed": None, "username": username}
        completed = todo.get("completed")
        title = todo.get("title")
        task.update(task=title, completed=completed)
        tasks.append(task)

    data.update({user_id: tasks})

    with open("{}.json".format(user_id), mode='wt', encoding='utf-8') as f:
        json.dump(data, f)
