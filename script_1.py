import csv
filename='convert_to_vcf.csv'#input file
n=359 #total number of contacts
with open(filename, 'rb') as f:
	reader=csv.reader(f)
	my_list=list(reader)
	

datafile=open('new_vcf.vcf','w')
for i in range(0,359):
	s='\nBEGIN:VCARD\nVERSION:2.1\nN:'+my_list[i][0].split(' ')[1]+';'+my_list[i][0].split(' ')[0]+';;;\nFN:'+my_list[i][0]+'\nTEL;CELL:'+my_list[i][1]+'\nEND:VCARD'
	datafile.write(s)



datafile.close()



