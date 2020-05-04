#!/usr/bin/python3

"""Export to CSV data from the previous task"""

if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    req_user_todo = requests.get("{}/users/{}/todos".format(base_url, user_id))
    req_user_info = requests.get("{}/users/{}".format(base_url, user_id))

    data_user_todo = req_user_todo.json()
    data_user_info = req_user_info.json()
    name = data_user_info.get("name")

    csv_list = []
    for todo in data_user_todo:
        completed = todo.get("completed")
        title = todo.get("title")
        new = '"{}","{}","{}","{}"'.format(
            user_id, name, str(completed), title)
        csv_list.append(new)

    with open("{}.csv".format(user_id), mode='wt', encoding='utf-8') as f:
        f.write('\n'.join(line for line in csv_list))
        f.write('\n')