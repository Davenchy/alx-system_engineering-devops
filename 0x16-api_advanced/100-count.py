#!/usr/bin/python3
"""sort and search hot articles of a subreddit"""
import requests


def count_words(subreddit, word_list, after=None, count=0, begin=True):
    """fetch all reddit hot posts of a subreddit

    Args:
        subreddit (str): the subreddit name
        word_list (list): the list of words to search for each in articles
            titles
        after (str): the next article to start from
        count (int): the number of articles to have in the list"""

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
    titles = list(map(lambda c: c['data']['title'], children))

    count += data.get('dist', 0)
    after = data.get('after')

    matches = {}
    for word in word_list:
        for title in titles:
            if word not in matches:
                matches[word] = 0
            matches[word] += title.lower().count(word.lower())

    if after is not None:
        r_matches = count_words(subreddit, word_list, after, count, False)
        for k, v in r_matches.items():
            matches[k] += v

    if not begin:
        return matches

    sorted_matches = sorted(matches.items(), key=lambda x: x[1], reverse=True)
    [print(f'{m[0]}: {m[1]}') for m in sorted_matches if m[1] > 0]
