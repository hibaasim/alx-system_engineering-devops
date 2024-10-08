#!/usr/bin/python3
'''Module to query the Reddit API and return the number of subscribers'''

import requests


def number_of_subscribers(subreddit):
    '''Gives the number of subscribers for a valid subreddit

    Args:
        subreddit: name of the subreddit
    '''
    base_url = 'https://www.reddit.com/r/'

    url = '{}{}/about.json'.format(base_url, subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
