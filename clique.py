from data_preparation import Data
from basic_grouping import BasicGrouping
import config
from collections import defaultdict

data = Data()
basic_grouping = BasicGrouping()
challenge, serial_dict = data.get_challenges(config.challenges_path)
submissions = data.get_submissions(config.submissions_path, serial_dict)
submissions_train, submissions_test = data.divide_test_train(config.ratio, submissions)

challeneges_by_user = basic_grouping.get_challenges_per_user(submissions_train)

user_list = data.get_user_list(submissions_train)
co_occurence = {}

def update(challenge_list, co_occurence):
	length = len(challenge_list)
	keys = co_occurence.keys()
	print length
	for item1 in challenge_list:
		index = challenge_list.index(item1)
		for item2 in challenge_list[index:]:
			pair1 = (item1, item2)
			pair2 = (item2, item1)
			if pair1 in keys:
				co_occurence[pair1]+=1
			elif pair2 in keys:
				co_occurence[pair2]+=1
			else:
				co_occurence[pair1] = 1
	return co_occurence

for user in user_list:
	challenge_list = challeneges_by_user[user].keys()
	if challenge_list:
		#print challenge_list
		co_occurence = update(challenge_list, co_occurence)
	#print co_occurence
print {k: co_occurence[k] for k in co_occurence.keys()[:5]}