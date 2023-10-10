#!/usr/bin/python3
"""use reddit api to fetch all subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """get number of subscribers of a subreddit

    Args:
        subreddit (str): the subreddit name

    Return (int): the number of subscribers"""

    res = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={'User-Agent': 'alx:dev.davenchy:v1.0'},
    )
    if not res.ok:
        return 0
    return res.json()['data']['subscribers']
