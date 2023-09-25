#!/usr/bin/python3
""" Python script that takes user id and saves all tasks into csv file """

import requests
import csv
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


def getTasks(user_id):
    """ get tasks owned by user using its id

    Args:
        user_id (int): user's id

    Returns: tasks (list)"""

    res = requests.get("{}/users/{}/todos".format(BASE_URL, user_id))
    tasks = res.json()

    return tasks or list()


def saveCSV(user_id, username, tasks):
    """ generate csv and save it to file with name "USER_ID.csv"

    Args:
        user_id (int): user's id
        username (str): user's name
        tasks (list): list of tasks

    Returns: None"""

    with open("{}.csv".format(user_id), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # row format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        for task in tasks:
            row = [user_id, username, task.get("completed"), task.get("title")]
            writer.writerow(row)


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

    # get user information
    username = getUsername(user_id)
    tasks = getTasks(user_id)

    # save to csv file
    saveCSV(user_id, username, tasks)
