from data_preparation import Data
from basic_grouping import BasicGrouping
import config
from collections import defaultdict
from sklearn import datasets, linear_model
from sklearn import preprocessing

data = Data()
basic_grouping = BasicGrouping()
challenge, serial_dict = data.get_challenges(config.challenges_path)
challenge_X = data.get_challenge_X(config.challenges_path)
submissions = data.get_submissions(config.submissions_path, serial_dict)
submissions_train, submissions_test = data.divide_test_train(config.ratio, submissions)

challeneges_by_user = basic_grouping.get_challenges_per_user(submissions_train)

def get_coeff(user):
	item = challeneges_by_user[user]
	X_train = []
	Y_train = []
	for problem in item:
		X_train.append(challenge_X[problem.keys()[0]][:2])
		Y = int(problem.values()[0])
		Y_train.append((Y*3)+2)
	regr = linear_model.LinearRegression()
	regr.fit(X_train, Y_train)
	coeff = regr.coef_
	return coeff

def recommend(user):
	coeff =  get_coeff(user)
	challenge_weight = []
	for item in challenge:
		weight = (coeff[0]*float(item['difficulty']))+(coeff[1]*float(item['submitted']))
		challenge_weight.append({item['id']: weight})
	challenge_weight = sorted(challenge_weight, key=getKey)

	return [item.keys()[0] for item in challenge_weight[:10]]

def getKey(item):
	return item.values()[0]

user = '615e39b050307505'

#This will recommend ten challenges to user
for user in challeneges_by_user.keys():
	print {'user': user, 'reco': recommend(user)}