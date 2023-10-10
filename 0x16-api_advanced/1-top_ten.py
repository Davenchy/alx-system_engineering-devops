#!/usr/bin/python3
"""script that uses reddit api to fetch top 10 titles of a subreddit"""
import requests


def top_ten(subreddit):
    """prints the top 10 titles of a subreddit

    Args:
        subreddit (str): the subreddit name"""
    res = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
        headers={'User-Agent': 'alx:dev.davenchy:v1.0 (by /u/davenchy)'},
        allow_redirects=False,
    )
    if not res.ok:
        print("None")
        return
    [print(c['data']['title']) for c in res.json()['data']['children']]
