from basic_grouping import BasicGrouping
from data_preparation import Data
from validation import Validation
import config


##This is very basic model. Just to get started and get infra ready
###### Algo1 implementation#####
input_data = Data()
basic_group_algo = BasicGrouping()

challenges, serial_dict = input_data.get_challenges(config.challenges_path)
submissions = input_data.get_submissions(config.submissions_path, serial_dict)
submissions_train, submissions_test = input_data.divide_test_train(0.7, submissions)
challenges = basic_group_algo.sort_data(challenges)

group_dict = basic_group_algo.create_group_dict(challenges, 'challenge_id')

#user_dict = get_challenges_per_user(submissions)
user_groups = basic_group_algo.get_groups_per_user(submissions_train, group_dict)
group_challenge_dict =  basic_group_algo.get_challenges_per_group(group_dict)

user_reco_dict = input_data.get_user_dict(submissions_train)

for user, data in user_reco_dict.iteritems():
	user_suggestions = basic_group_algo.get_suggestions(user_groups[user], group_challenge_dict)
	user_reco_dict[user].extend(user_suggestions)


#This will give recommendation for each user
for user, item in user_reco_dict.iteritems():
	print {'user': user, 'reco': item}
###############