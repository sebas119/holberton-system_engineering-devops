#!/usr/bin/python3

"""Export to JSON data of all todos and all users"""

if __name__ == "__main__":
    import requests
    import sys
    import json

    base_url = "https://jsonplaceholder.typicode.com"

    req_todos = requests.get("{}/todos".format(base_url))
    req_users = requests.get("{}/users".format(base_url))

    data_todos = req_todos.json()
    data_users = req_users.json()

    data = {}
    for user in data_users:
        user_id = user.get("id")
        username = user.get("username")
        task = []
        for todo in data_todos:
            if user_id == todo.get("userId"):
                temp_dict = {"task": "", "completed": None,
                             "username": username}
                completed = todo.get("completed")
                title = todo.get("title")
                temp_dict.update({"task": title, "completed": completed})
                task.append(temp_dict)
        data.update({user_id: task})

    with open("todo_all_employees.js", mode='wt', encoding='utf-8') as f:
        json.dump(data, f)
