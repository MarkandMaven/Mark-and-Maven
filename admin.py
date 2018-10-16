# Administrative Functions for Mark and Maven Networks

import random
import csv
import string
import json

root = 'C:/Users/holtb/Desktop/Mark and Maven/' # location of the mavenOS root file

def idCreate():
	idTaken = idList()
	idNew = ''.join(random.choices(string.ascii_uppercase + string.digits, k=14))
	while idNew in idTaken:
		idNew = ''.join(random.choices(string.ascii_uppercase + string.digits, k=14))
	return idNew

def exportCreate(root, filename, content):
	address = root + 'exports/' + filename + '.txt'	
	with open(address, 'w', newline='') as writefile:
		createWriter = csv.writer(writefile)
		createWriter.writerow(content)
	return	

def idList():
	IDs = []
	profile = upload(root, 'IJPM2AAHJR4YXN')
	for i in profile:
		if i[0] == 'connection':
			IDs.append(i[1])
	return IDs # returns a list of IDs that have already been taken

def upload(root, ID):
	content = []
	address = root + 'nodes/' + ID + '.txt'
	with open(address, 'r', newline='') as readfile:
		uploadReader = csv.reader(readfile)
		for i in uploadReader:
			content.append(i)
	return content

def nodeCreate(profile):
	address = root + 'nodes/' + profile[0][1] + '.txt'	
	with open(address, 'w', newline='') as writefile:
		createWriter = csv.writer(writefile)
		for i in profile:
			createWriter.writerow(i)
	return

def nodeUpdate(ID, update): # (str, dict)
	address = root + 'nodes/' + ID + '.txt'	
	with open(address, 'a', newline='') as writefile:
		updateWriter = csv.writer(writefile)
		updateWriter.writerow(update)
	return

def importCreate(root, filename):
	content = []
	address = root + 'imports/' + filename + '.net'	
	with open(address) as readfile:
		for i in readfile:
			content.append(json.loads(i))
	return content
