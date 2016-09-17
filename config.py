import os
os.path.abspath
challenges_path = os.path.abspath('challenges.csv')
submissions_path = os.path.abspath('submissions.csv')
ratio = 0.7

domain_serial = {
	'C++': 0,
	'Databases': 1,
	'Distributed Systems':2,
	'Functional Programming': 3,
	'Java': 4,
	'Linux Shell': 5,
	'Mathematics': 6,
	'Python': 7,
	'Regex': 8,
	'Ruby': 9,
	'Security': 10,
	'SQL': 11,
	'Tutorials': 12,
	'Bit Manipulation': 13,
	'Dynamic Programming': 14,
	'Game Theory': 15,
	'Graph Theory': 16,
	'Greedy': 17,
	'Implementation': 18,
	'NP Complete': 19,
	'Search': 20,
	'Sorting': 21,
	'Strings': 22,
	'Warmup': 23,
	'Advanced': 24,
	'Arrays': 25,
	'Balanced Trees': 26,
	'Disjoint Set' : 27,
	'Heap': 28,
	'Linked Lists': 29,
	'Queues': 30,
	'Stacks': 31,
	'Trees': 32,
	'Trie': 33,
	'Random': 34
}