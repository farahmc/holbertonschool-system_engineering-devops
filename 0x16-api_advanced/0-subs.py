#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ return number of subscribers
    if not a valid subreddit, return 0
    do not follow redirects """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
    url = "https://www.reddit.com/r/{}/about.json".format(argv[1])
    r_subs = requests.get(url, headers=headers)
    if r_subs.ok is False:
        return 0

    subs = r_subs.json()
    for k, v in subs['data'].items():
        if k == "subscribers":
            number_of_subs = v
    return(number_of_subs)

