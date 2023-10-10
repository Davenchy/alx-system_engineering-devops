#!/usr/bin/python3
"""fetch all reddit hot posts of a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """fetch all reddit hot posts of a subreddit

    Args:
        subreddit (str): the subreddit name
        hot_list (list): the list of hot posts
        after (str): the last post id

    Return (list): the list of hot posts"""
    params = {'limit': 100, 'count': count}
    if after:
        params['after'] = after

    res = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={'User-Agent': 'alx:dev.davenchy:v1.0 (by /u/davenchy)'},
        params=params,
        allow_redirects=False,
    )

    if not res.ok:
        return None

    data = res.json()['data']
    children = data.get('children')
    hot_list.extend(map(lambda c: c['data']['title'], children))

    count += data.get('dist', 0)
    after = data.get('after')

    if after is not None:
        recurse(subreddit, hot_list, after, count)

    return hot_list
