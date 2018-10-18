import json
import csv

with open('venmo.json', 'r') as read_file:
	data = json.load(read_file)

csv_data = open('venmo.csv', 'w')

fieldnames = ['datetime_created', 'note', 'amount', 'type', 'actor', 'action', 'target']

writer = csv.DictWriter(csv_data, fieldnames=fieldnames)
writer.writeheader()

for transaction in data['data']['transactions']:
	trans = {}
	trans['datetime_created'] = transaction['datetime_created']
	trans['note'] = transaction['note']
	trans['amount'] = transaction['amount']
	trans['type'] = transaction['type']
	if transaction['payment']:
		trans['actor'] = transaction['payment']['actor']['display_name']
		trans['action'] = transaction['payment']['action']
		trans['target'] = transaction['payment']['target']['user']['display_name']

	writer.writerow(trans)	

csv_data.close()
