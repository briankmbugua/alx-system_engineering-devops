#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
    """returns number of subscribers for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "python:number_of_subscribers (by u/briankinyanjui)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:

        return 0


if __name__ == "__main__":
    print(number_of_subscribers(sys.argv[1]))
