#Edited by Joseph Antony Protus, Sathya
import csv
Actual_List=[]
count=0
Expected_List=['True','False','False','True','True','True','True','True','False','False','True','True','True','True']
with open('OUTPUT.csv') as f:
	rows = csv.reader(f)
	for row in rows:
		Actual_List.append(row[1])
for i in range(14):
	if Actual_List[i]==Expected_List[i]:
		count+=1
print count 