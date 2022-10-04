#!/usr/bin/python3
""" queries the Reddit API and returns a list containing the
 titles of all hot articles for a given subreddit """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function that returns a list of titles
    if not a valid subreddit, return None
    do not follow redirects """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    r_hot = requests.get(url, headers=headers, allow_redirects=False)
    if r_hot.ok is False:
        return None

    hot_posts = r_hot.json()
    all_posts = hot_posts['data']['children']
    for post in all_posts:
        hot_list.append(post['data']['title'])
    after = hot_posts['data']['after']
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
