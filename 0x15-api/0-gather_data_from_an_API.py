#!/usr/bin/python3
""" Python script that takes user id and show all completed TODOs that user """

import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


def getUsername(user_id):
    """ get username by its id

    Args:
        user_id (int): user id

    Returns: username(str)"""

    res = requests.get("{}/users/{}".format(BASE_URL, user_id))
    user_info = res.json()

    return user_info.get("name")


def getTodosInfo(user_id):
    """ get todos info by user's id

    Args:
        user_id (int): user id

    Returns:
        (todos_count: int, completed_count: int, completed_todos: list)"""
    res = requests.get("{}/users/{}/todos".format(BASE_URL, user_id))
    todos_info = res.json()
    total_count, completed_count, completed_todos = 0, 0, list()

    for todo in todos_info:
        total_count += 1
        if todo.get("completed"):
            completed_count += 1
            completed_todos.append(todo.get("title"))

    return (total_count, completed_count, completed_todos)


if __name__ == "__main__":
    # validate that user uses the tool correctly
    if len(sys.argv) != 2:
        print("Usage: {} <id>".format(sys.argv[0]), file=sys.stderr)
        exit(1)

    user_id = sys.argv[1]  # get user id

    # try to parse the user id
    try:
        user_id = int(user_id)
    except ValueError:
        print("Not a valid ID", file=sys.stderr)
        exit(1)

    # print user information
    username = getUsername(user_id)
    total_count, completed_count, completed_todos = getTodosInfo(user_id)
    print("Employee {} is done with tasks({}/{}):".format(
        username, completed_count, total_count))

    # print completed todos
    for todo in completed_todos:
        print("\t {}".format(todo))
