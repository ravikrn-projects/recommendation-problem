import random 
from collections import defaultdict

class Validation:

	def __init__(self, recommended_data, test_dataset, challenges):
		self.recommended_data = recommended_data
		self.test_dataset =  test_dataset
		self.challenges = challenges
		self.challenge_list = self.challenge_list()

	def intersection(self, recommended, actual):
		return [challenge for challenge in actual if challenge in recommended]

	def challenge_list(self):
		challenge_list = []
		for challenge in self.challenges:
			challenge_list.append(challenge['challenge_id'])
		return challenge_list

	def user_score(self, recommended, actual):
		model_intersection = len(self.intersection(recommended, actual))
		random_recommendation = random.sample(self.challenge_list, 10)
		random_intersection = len(self.intersection(random_recommendation, actual))
		if model_intersection == 0 & random_intersection == 0:
			return -1
		else:
			print 'test'
			return (model_intersection)/(random_recommendation+model_intersection)

	def test_data_refined(self):
		test_data_list = defaultdict(list)
		for item in self.test_dataset:
			test_data_list[item['hacker_id']].append(item['challenge'])
		return test_data_list

	#recommended_data will be defaultdict with user and key		
	def score(self):
		test_data_list = self.test_data_refined()
		score = 0
		for user, recommendation in self.recommended_data.iteritems():
			score =  score + self.user_score(recommendation, test_data_list['user'])
		count = sum([1 for i,j in self.recommended_data.iteritems()])
		return float(score)/count
