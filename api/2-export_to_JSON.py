#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_endpoint = "users/{}".format(user_id)
    todos_endpoint = "todos"

    user_url = urllib.parse.urljoin(base_url, user_endpoint)
    todos_url = urllib.parse.urljoin(base_url, todos_endpoint)

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())
        username = user.get("username")

    todos_params = {"userId": user_id}
    new = todos_url + "?" + urllib.parse.urlencode(todos_params)
    with urllib.request.urlopen(new) as response:
        todos = json.loads(response.read().decode())

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(
            {
                user_id: [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": username
                    }
                    for t in todos
                ]
            },
            jsonfile,
        )
