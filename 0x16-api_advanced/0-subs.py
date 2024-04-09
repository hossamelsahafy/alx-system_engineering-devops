#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
"""
import requests


def number_of_subscribers(subreddit):
    """Get The Number Of Subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/Young_68)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']
