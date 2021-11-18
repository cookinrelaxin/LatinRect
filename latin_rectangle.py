import csv

EXP0 	= 'Experimental Item'
SS1 	= 'SS'
SP2 	= 'SP'
SSS3 	= 'SSS'
SPS4 	= 'SPS'
SSP5 	= 'SSP'
SPP6 	= 'SPP'
SSA7 	= 'SSA'
SPA8 	= 'SPA'
fields = [EXP0, SS1, SP2, SSS3, SPS4, SSP5, SPP6, SSA7, SPA8]

def read_items(name, separator):
	items = []

	with open(name) as file:
		reader = csv.DictReader(file, delimiter=separator)
		for row in reader:
			items.append(row)

	assert len(items) == 80
	return items

def make_rectangle(arr):

	assert len(arr) == 80

	combs = [
			[SS1, 	SP2, 	SSS3, 	SPS4, 	SSP5, 	SPP6, 	SSA7, 	SPA8],
			[SP2, 	SSS3, 	SPS4, 	SSP5, 	SPP6, 	SSA7, 	SPA8, 	SS1],
			[SSS3, 	SPS4, 	SSP5, 	SPP6, 	SSA7, 	SPA8, 	SS1, 	SP2],
			[SPS4, 	SSP5, 	SPP6, 	SSA7, 	SPA8, 	SS1, 	SP2, 	SSS3],
			[SSP5, 	SPP6, 	SSA7, 	SPA8, 	SS1, 	SP2, 	SSS3, 	SPS4],
			[SPP6, 	SSA7, 	SPA8, 	SS1, 	SP2, 	SSS3, 	SPS4, 	SSP5],
			[SSA7, 	SPA8, 	SS1, 	SP2, 	SSS3, 	SPS4, 	SSP5, 	SPP6],
			[SPA8, 	SS1, 	SP2, 	SSS3, 	SPS4, 	SSP5, 	SPP6, 	SSA7]]

	lists = [	[], [], [], [],
			[], [], [], []]

	j = 0

	for i in range(0, 80):

		if 10 < i <= 20:
			j = 1
		if 20 < i <= 30:
			j = 2
		if 30 < i <= 40:
			j = 3
		if 40 < i <= 50:
			j = 4
		if 50 < i <= 60:
			j = 5
		if 60 < i <= 70:
			j = 6
		if 70 < i <= 80:
			j = 7
		
		dict = arr[i]
		for k in range (0, 8):
			condition = combs[j][k]
			lists[k].append({condition: dict[condition]})

	for i in range (0, 8):		
		assert len(lists[i]) == 80

	for i in range(0, 8):
		name = 'list'+str(i+1)+'.csv'
		with open(name, 'w', newline='') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=fields)		
			writer.writeheader()
			for j in range(0, 80):
				writer.writerow(lists[i][j])

def main():
	items = read_items("Experimental Items.csv", ",")
	make_rectangle(items)

if __name__ == "__main__":
	main()