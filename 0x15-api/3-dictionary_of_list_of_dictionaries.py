#!/usr/bin/python3
""" Python script that fetch all users tasks and saves them into json file """

import json
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"
FILENAME = "todo_all_employees"


def loadAllUsers():
    """ load all users from api

    Returns: users (list)"""

    res = requests.get("{}/users".format(BASE_URL))
    users = res.json()

    return users


def getTasks(user_id):
    """ get tasks owned by user using its id

    Args:
        user_id (int): user's id

    Returns: tasks (list)"""

    res = requests.get("{}/users/{}/todos".format(BASE_URL, user_id))
    tasks = res.json()

    return tasks or list()


def saveJSON(user_id, username, tasks):
    """ generate json and save it to file with name "USER_ID.json"

    Args:
        user_id (int): user's id
        username (str): user's name
        tasks (list): list of tasks

    Returns: None"""

    with open("{}.json".format(user_id), "w", newline="") as file:
        formatedTasks = [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in tasks]
        jsonData = {str(user_id): formatedTasks}

        json.dump(jsonData, file)


def formatUserTask(task, username):
    """ format user task

    Args:
        task (dict): task
        username (str): username

    Returns:
        (dict): formatted task
    """
    return {
        "username": username,
        "task": task.get("title"),
        "completed": task.get("completed"),
    }


if __name__ == "__main__":
    # get all users
    users = loadAllUsers()
    data = {}

    # get tasks and format
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        tasks = getTasks(user_id)
        tasks = map(lambda t: formatUserTask(t, username), tasks)
        data[user_id] = list(tasks)

    # save to json file
    with open("{}.json".format(FILENAME), "w", newline="") as file:
        json.dump(data, file)
