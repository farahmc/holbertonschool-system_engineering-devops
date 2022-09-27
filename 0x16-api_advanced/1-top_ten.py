#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the
 first 10 hot posts listed for a given subreddit """
import requests


def top_ten(subreddit):
    """ return titles of first 10 hot posts
    if not a valid subreddit, print None
    do not follow redirects """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r_hot = requests.get(url, headers=headers, allow_redirects=False)
    if r_hot.ok is False:
        print("None")
        return None

    hot_posts = r_hot.json()
    top_10 = []
    for i in range(10):
        top_10.append(hot_posts['data']['children'][i]['data']['title'])
    for title in top_10:
        print(title)
    return 1
