#import problems from challenges
import csv
from collections import defaultdict
from data_preparation import Data
import config

class BasicGrouping: 
	def __init__(self):
		pass

	def get_challenges_per_user(self, submissions):
		user_dict = defaultdict(list)
		for submission in submissions:
			user_dict[submission['hacker_id']].append({submission['challenge_serial']: int(submission['solved'])})
		return user_dict

	def get_groups_per_user(self, submissions, group_dict):
		user_dict = defaultdict(set)
		for submission in submissions:
			try:
				group_id = group_dict[submission['challenge']]
			except KeyError:			
				continue
			user_dict[submission['hacker_id']].add(group_id)
		return user_dict

	def get_challenges_per_group(self, group_dict):
		group_challenge_dict = defaultdict(list)
		for challenge, group in group_dict.iteritems():
			group_challenge_dict[group].append(challenge)
		return group_challenge_dict

	def get_suggestions(self, user_groups, group_challenge_dict):
		suggestions = set([])
		for group in user_groups:
			suggestions = suggestions.union(set(group_challenge_dict[group]))
		return list(suggestions)[:10]

	def create_group_dict(self, data, key):
		group_dict = {}
		for i in range(len(data)):
			group_dict[data[i][key]] = (i+1)/20
		return group_dict

	def getkey(self, item):
		return item['difficulty']

	def sort_data(self, data):
		return sorted(data, key=self.getkey)