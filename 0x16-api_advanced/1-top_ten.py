#!/usr/bin/python3
"""script that uses reddit api to fetch top 10 titles of a subreddit"""
import requests


def top_ten(subreddit):
    """prints the top 10 titles of a subreddit

    Args:
        subreddit (str): the subreddit name"""
    res = requests.get(
        f"https://www.reddit.com/r/{subreddit}/top.json?limit=10",
        headers={'User-Agent': 'alx:dev.davenchy:v1.0'},
    )
    if not res.ok:
        print("None")
        return

    children = res.json()['data']['children']
    for child in children:
        print(child['data']['title'])
