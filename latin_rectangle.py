import csv

def read_items(name, separator):
	items = []

	with open(name) as file:
		reader = csv.DictReader(file, delimiter=separator)
		for row in reader:
			item = []
			item.append(row["Experimental Item"])

			item.append(row["SS"])
			item.append(row["SP"])
			item.append(row["SSS"])
			item.append(row["SPS"])

			item.append(row["SSP"])
			item.append(row["SPP"])
			item.append(row["SSA"])
			item.append(row["SPA"])

			items.append(item)

	assert len(items) == 80
	return items

def make_rectangle(arr):

	assert len(arr) == 80

	comb1 = [1, 2, 3, 4, 5, 6, 7, 8]
	comb2 = [2, 3, 4, 5, 6, 7, 8, 1]
	comb3 = [3, 4, 5, 6, 7, 8, 1, 2]
	comb4 = [4, 5, 6, 7, 8, 1, 2, 3]
	comb5 = [5, 6, 7, 8, 1, 2, 3, 4]
	comb6 = [6, 7, 8, 1, 2, 3, 4, 5]
	comb7 = [7, 8, 1, 2, 3, 4, 5, 6]
	comb8 = [8, 1, 2, 3, 4, 5, 6, 7]

	list1 = []	
	list2 = []
	list3 = []
	list4 = []
	list5 = []
	list6 = []
	list7 = []
	list8 = []

	for i in range(0, 10):
		ss = arr[i]

		list1.append(ss[comb1[0]])
		list2.append(ss[comb1[1]])
		list3.append(ss[comb1[2]])
		list4.append(ss[comb1[3]])
		list5.append(ss[comb1[4]])
		list6.append(ss[comb1[5]])
		list7.append(ss[comb1[6]])
		list8.append(ss[comb1[7]])

	for i in range(10, 20):
		ss = arr[i]

		list1.append(ss[comb2[0]])
		list2.append(ss[comb2[1]])
		list3.append(ss[comb2[2]])
		list4.append(ss[comb2[3]])
		list5.append(ss[comb2[4]])
		list6.append(ss[comb2[5]])
		list7.append(ss[comb2[6]])
		list8.append(ss[comb2[7]])

	for i in range(20, 30):
		ss = arr[i]

		list1.append(ss[comb3[0]])
		list2.append(ss[comb3[1]])
		list3.append(ss[comb3[2]])
		list4.append(ss[comb3[3]])
		list5.append(ss[comb3[4]])
		list6.append(ss[comb3[5]])
		list7.append(ss[comb3[6]])
		list8.append(ss[comb3[7]])

	for i in range(30, 40):
		ss = arr[i]

		list1.append(ss[comb4[0]])
		list2.append(ss[comb4[1]])
		list3.append(ss[comb4[2]])
		list4.append(ss[comb4[3]])
		list5.append(ss[comb4[4]])
		list6.append(ss[comb4[5]])
		list7.append(ss[comb4[6]])
		list8.append(ss[comb4[7]])

	for i in range(40, 50):
		ss = arr[i]

		list1.append(ss[comb5[0]])
		list2.append(ss[comb5[1]])
		list3.append(ss[comb5[2]])
		list4.append(ss[comb5[3]])
		list5.append(ss[comb5[4]])
		list6.append(ss[comb5[5]])
		list7.append(ss[comb5[6]])
		list8.append(ss[comb5[7]])

	for i in range(50, 60):
		ss = arr[i]

		list1.append(ss[comb6[0]])
		list2.append(ss[comb6[1]])
		list3.append(ss[comb6[2]])
		list4.append(ss[comb6[3]])
		list5.append(ss[comb6[4]])
		list6.append(ss[comb6[5]])
		list7.append(ss[comb6[6]])
		list8.append(ss[comb6[7]])

	for i in range(60, 70):
		ss = arr[i]

		list1.append(ss[comb7[0]])
		list2.append(ss[comb7[1]])
		list3.append(ss[comb7[2]])
		list4.append(ss[comb7[3]])
		list5.append(ss[comb7[4]])
		list6.append(ss[comb7[5]])
		list7.append(ss[comb7[6]])
		list8.append(ss[comb7[7]])

	for i in range(70, 80):
		ss = arr[i]

		list1.append(ss[comb8[0]])
		list2.append(ss[comb8[1]])
		list3.append(ss[comb8[2]])
		list4.append(ss[comb8[3]])
		list5.append(ss[comb8[4]])
		list6.append(ss[comb8[5]])
		list7.append(ss[comb8[6]])
		list8.append(ss[comb8[7]])

	assert len(list1) == 80
	assert len(list2) == 80
	assert len(list3) == 80
	assert len(list4) == 80
	assert len(list5) == 80
	assert len(list6) == 80
	assert len(list7) == 80
	assert len(list8) == 80

	with open('latin_rectangle.csv', 'w', newline='') as csvfile:
		fieldnames = ['Experimental Item', 'SS', 'SP', 'SSS', 'SPS', 'SSP', 'SPP', 'SSA', 'SPA']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		writer.writeheader()

		##WRONG##
		for i in range(0, 80):
			writer.writerow({'Experimental Item':	arr[i][0],
					'SS':			list1[i],
					'SP':			list2[i],
					'SSS':			list3[i],
					'SPS':			list4[i],
					'SSP':			list5[i],
					'SPP':			list6[i],
					'SSA':			list7[i],
					'SPA':			list8[i]})

def main():
	items = read_items("Experimental Items.csv", ",")
	make_rectangle(items)

if __name__ == "__main__":
	main()