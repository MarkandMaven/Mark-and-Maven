# Administrative Functions for Mark and Maven Networks

import random
import csv
import string

root = 'C:/Users/holtb/Desktop/mavenOS/' # location of the mavenOS root file

def idCreate():
	idTaken = idList()
	idNew = ''.join(random.choices(string.ascii_uppercase + string.digits, k=14))
	while idNew in idTaken:
		idNew = ''.join(random.choices(string.ascii_uppercase + string.digits, k=14))
	return idNew

def exportCreate(filename, content):
	address = root + 'exports/' + filename + '.txt'	
	with open(address, 'w', newline='') as writefile:
		createWriter = csv.writer(writefile)
		createWriter.writerow(content)
	return	

def idList():
	IDs = []
	profile = upload('IJPM2AAHJR4YXN')
	for i in profile:
		if i[0] == 'connection':
			IDs.append(i[1])
	return IDs # returns a list of IDs that have already been taken

def upload(ID):
	content = []
	address = root + ID + '.txt'
	with open(address, 'r', newline='') as readfile:
		uploadReader = csv.reader(readfile)
		for i in uploadReader:
			content.append(i)
	return content

def nodeCreate(profile):
	address = root + profile[0][1] + '.txt'	
	with open(address, 'w', newline='') as writefile:
		createWriter = csv.writer(writefile)
		for i in profile:
			createWriter.writerow(i)
	return

def nodeUpdate(ID, update): # (str, dict)
	address = root + ID + '.txt'	
	with open(address, 'a', newline='') as writefile:
		updateWriter = csv.writer(writefile)
		updateWriter.writerow(update)
	return