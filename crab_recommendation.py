from data_preparation import Data
from basic_grouping import BasicGrouping
import config
from collections import defaultdict
from scikits.crab.models import MatrixPreferenceDataModel
from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
from scikits.crab.recommenders.knn import UserBasedRecommender


data = Data()
basic_grouping = BasicGrouping()
challenge, serial_dict = data.get_challenges(config.challenges_path)
submissions = data.get_submissions(config.submissions_path, serial_dict)
submissions_train, submissions_test = data.divide_test_train(config.ratio, submissions)
user_list = data.get_user_list(submissions_train)

def get_challenges_user(submissions_train):
	user_dict = {}
	for submission in submissions_train:
		try:
			user_dict[submission['hacker_id']][submission['challenge']] = submission['solved']
		except KeyError:
			user_dict[submission['hacker_id']] = {submission['challenge']: submission['solved']}
	return user_dict
user_data = get_challenges_user(submissions_train)
model = MatrixPreferenceDataModel(user_data)
similarity = UserSimilarity(model, pearson_correlation)
recommender = UserBasedRecommender(model, similarity, with_preference=True)

for user in user_list:
	print recommender.recommend(user)