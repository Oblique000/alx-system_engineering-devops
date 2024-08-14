#!/usr/bin/python3
import requests

def top_ten(subreddit):
	headers = {'User-Agent': 'My User Agent 1.0'}
	url = f'https://www.reddit.com/r/{subreddit}/hot.json'
	params = {"limit": 10}

try:
	r = requests.get(url, headers=headers, params=params, allow_redirects=False)
	r.raise_for_status()
data = r.json()
	results = data.get("data", {})

	for i in results.get("children", []):
		title = i.get('data', {}).get('title', 'No title found')
print(title)
	except (requests.exceptions.HTTPError, ValueError):
		print(None)
