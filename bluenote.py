# github Blue Note project
# https://github.com/xentenza/bluenote
#
# Creating csv files for Gephi

import csv

#create export file

print ('>>> Creating edges-names.csv ...')

writer = csv.writer(open('edges-names.csv', 'a'))
header = ['Weight','Source','Target','Type','Alternate Take','Recorded','1st release','status']
writer.writerow(header)

# First of all, create file ith all combinations
# And also year of recording, number of tracks recorded

f = open('bn-data.csv')
csv_f = csv.reader(f)

x = 6 #we start at seventh column
y = x + 1

for row in csv_f: 
	while row[x] != '':
		try:
			row[y]
		except IndexError:
			break
		while row[y]:
			musician1 = row[x]
			musician2 = row[y]
			alternate = row[1]
			recorded = row[3]
			released = row[4]
			status = row[5]
			links = ['1',musician1,musician2,'Undirected',alternate,recorded,released,status]
			writer = csv.writer(open('edges-names.csv', 'a'))
			writer.writerow(links)
			y += 1
			try:
				row[y]
			except IndexError:
				break
		x += 1
		y = x + 1
	x = 6
	y = x + 1

print ('edges-names.csv complete')

# List of unique musicians (a.k.a. Nodes)

print ('>>> Creating nodes.csv ...')

writer = csv.writer(open('nodes.csv', 'a'))
header = ['ID','Label']
writer.writerow(header)

f = open('edges-names.csv')
csv_f = csv.reader(f)

muslist = []

first_row = next(csv_f) #Start at the second row
for row in csv_f: 
	musician = row[1]
	muslist.append(musician)
	musician = row[2]
	muslist.append(musician)
uniquemusicians = set(muslist)
n = 1
for i in uniquemusicians:
	idmusician = [n,i]
	writer = csv.writer(open('nodes.csv', 'a'))
	writer.writerow(idmusician)
	n += 1

print ('nodes.csv complete')


# Create Edges list

print ('>>> Creating edges.csv ...')

import re

with open('edges-names.csv', 'r') as f:
    my_csv_text = f.read()
    new_csv_str = my_csv_text

f2 = open('nodes.csv')
csv_f = csv.reader(f2)

for row in csv_f: 
	find_str = "," + row[1] + "," #commas added to be sure we replace the full cell, not part of the string
	replace_str = "," + row[0] + ","
	new_csv_str = re.sub(find_str, replace_str, new_csv_str)

print ('Be patient, half of the job done :)')

f2 = open('nodes.csv')
csv_f = csv.reader(f2)

for row in csv_f: #run a second time for missed strings (when an artist "plays with himself")
	find_str = "," + row[1] + "," 
	replace_str = "," + row[0] + ","
	new_csv_str = re.sub(find_str, replace_str, new_csv_str)

new_csv_path = 'edges.csv'
with open(new_csv_path, 'w') as f:
	f.write(new_csv_str)

print ('edges.csv complete')

