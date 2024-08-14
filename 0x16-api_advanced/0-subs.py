#!/usr/bin/python3

""" get number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ get tge number of sub of s subreddit """
    headers = {
        'User-Agent': 'My-User-Agent'
    }
    url = 'https://www.reddit.com/r/{s}/about.json'.format(s=subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code < 300:
            data = response.json()
            return data.get("data").get("subscribers") 
        else:
            return 0
    except requests.RequestException as e:
        return 0
