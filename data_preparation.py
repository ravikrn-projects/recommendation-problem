import csv
import config
import random
from collections import defaultdict
from sklearn.preprocessing import OneHotEncoder

class Data:

	def __init__(self):
		self.serial_dict = {}

	def get_challenges(self, path):		
		with open(path, 'rb') as csvfile:
			line = csv.reader(csvfile)
			next(line)
			serial = 0
			serial_dict = {}
			challenges = []
			for row in line:
				row_dict = {}
				row_dict['challenge_id'] = row[0]
				row_dict['contest_id'] =  row[1]
				row_dict['domain'] =  row[2]
				row_dict['sub_domain'] =  row[3]
				row_dict['difficulty'] =  row[4]
				row_dict['solved'] =  row[5]
				row_dict['submitted'] =  row[6]
				row_dict['new_domain'] = config.domain_serial[self.get_new_domain(row)]
				row_dict['id'] = serial
				serial_dict[row[0]] = serial
				challenges.append(row_dict)
				serial += 1
			return challenges, serial_dict

	def get_new_domain(self, row):
		temp_domain = row[2]
		if temp_domain in ['C++', 'Databases', 'Distributed Systems', 'Functional Programming',
		'Java', 'Linux Shell', 'Mathematics', 'Python', 'Regex', 'Ruby', 'Security', 'SQL', 'Tutorials']:
			return temp_domain
		elif temp_domain in ['Algorithms', 'Data Structures']:
			return row[3]
		else:
			return 'Random'

	def get_challenge_X(self, path):
		challenges = {}
		enc = OneHotEncoder()
		new_domain_list = []
		for i in range(len(config.domain_serial)):
			new_domain_list.append([i])
		enc.fit(new_domain_list)
		with open(path, 'rb') as csvfile:
			line = csv.reader(csvfile)
			next(line)
			serial = 1
			serial_dict = {}
			for row in line:
				new_domain = config.domain_serial[self.get_new_domain(row)]
				#creating indicator variable for categorical varibles
				cat = enc.transform([[new_domain]]).toarray().tolist()[0]
				challenges[serial] = [float(row[4]), float(row[6])]
				challenges[serial].extend(cat)
				serial += 1
			return challenges

	def get_submissions(self, path, serial_dict):
		submissions = []
		with open(path, 'rb') as csvfile:
			line = csv.reader(csvfile)
			next(line)
			for row in line:
				try:
					row_dict = {}
					row_dict['hacker_id'] = row[0]
					row_dict['contest_id'] =  row[1]
					row_dict['challenge'] =  row[2]
					row_dict['language'] =  row[3]
					row_dict['solved'] =  row[4]
					row_dict['created_at'] =  row[5]
					row_dict['challenge_serial'] = serial_dict[row[2]]
					submissions.append(row_dict)
				except:
					continue
			return submissions

	def divide_test_train(self, ratio, data):
		length = len(data)
		train_index = random.sample(range(length), int(length*ratio))
		data_train = []
		data_test = []
		for index in train_index:
			data_train.append(data[index])
			data[index] = 0
		for item in data:
			if item != 0:
				data_test.append(item)
		return data_train, data_test

	def get_data(self, serial_dict):
		challenges = self.get_challenges(config.challenges_path)
		submissions = self.get_submissions(config.submissions_path, serial_dict)
		return challenges, submissions

	def get_user_dict(self, data):
		user_list = defaultdict(list)
		for item in data:
			user_list[item['hacker_id']].extend([])
		return user_list

	def get_user_list(self, data):
		user_list = []
		for item in data:
			user_list.append(item['hacker_id'])
		return list(set(user_list))