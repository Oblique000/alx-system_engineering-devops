#!/usr/bin/python3
"""0-subs module"""
import requests

def number_of_subscribers(subreddit):
	"""
	number_of_subscribers: returns the number of subscribers
	(not active users, total subscribers)
	for a given subreddit.
	"""
	headers = {'User-Agent': 'My User Agent'}
	url = f'https://www.reddit.com/r/{subreddit}/about.json'

	try:
	response = requests.get(url, headers=headers)
response.raise_for_status()

	if response.header.get('Content-Type') == 'application.json; charset=utf-8':
data = response.json()
	subscribers_count = data.get('data', {}).get('subscribers', 0)
	return subscriber_count

	except requests.RequestException as e:
	print(f"An error occured: {e}")

	return 0
