#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    # set custom user-agent
    user_agent = '0x16-api_advanced-jmajetich'
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # custom user-agent avoids request limit
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    try:
        
        # load response unit from json and return number of subscribers
        data = r.json().get('data', {})
        return data.get('subscribers', 0)
    except (KeyError, ValueError):
        return 0

