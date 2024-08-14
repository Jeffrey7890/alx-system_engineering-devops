#!/usr/bin/python3

""" get number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ get tge number of sub of s subreddit """
    headers = {
        'User-Agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64;\
                rv:92.0) Gecko/20100101 Firefox/92.0'''
    }
    url = 'https://www.reddit.com/r/{s}/about.json'.format(s=subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        print(e)
        return 0
