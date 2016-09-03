import json


with open('test_data.txt', 'r') as content_file:
		orders = json.load(content_file)


for order in orders:
	print order
	