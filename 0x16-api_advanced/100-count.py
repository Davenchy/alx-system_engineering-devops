#!/usr/bin/python3
"""sort and search hot articles of a subreddit"""
import requests


def count_words(subreddit, word_list, after=None, matches={}):
    """fetch all reddit hot articles of a subreddit and count the number of
    times each word of word_list appears in the titles

    Args:
        subreddit (str): the subreddit name
        word_list (list): the list of words to search for each in articles
            titles
        after (str): the next article to start from
        matches (dict): the number of times each word of word_list appears in
            the titles"""
    res = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={'User-Agent': 'alx:dev.davenchy:v1.0 (by /u/davenchy)'},
        params={'limit': 100, 'after': after},
        allow_redirects=False,
    )

    if not res.ok:
        return

    data = res.json()['data']
    children = data.get('children')
    titles = list(map(lambda c: c['data']['title'], children))
    after = data.get('after')

    for word in word_list:
        key = word.lower()
        for title in titles:
            title = title.lower().split(' ')
            if key not in matches:
                matches[key] = 0
            matches[key] += title.count(key)

    if not after:
        sorted_matches = sorted(matches.items(), key=lambda x: x[1],
                                reverse=True)
        [print(f'{m[0]}: {m[1]}') for m in sorted_matches if m[1] > 0]
        return

    count_words(subreddit, word_list, after, matches)
