'''
Mark and Maven is a network of bots, jobs, companies, and people (each of them “nodes”). 
Nodes have operating systems and "profiles."
Profiles are sets of "attributes."
Attributes are characteristics/traits (as-yet undefined), experiences (as-yet undefined), and relationships (as-yet undefined) to other nodes.
mavenOS is the operating system for a bot in the network called Maven.
'''

import csv 
import random 
import datetime
import itertools
import operator
import random

import admin
import analyst

ID = 'IDK2JJSBMTCO8E' # maven's ID number
root = 'C:/Users/holtb/Desktop/Mark and Maven/' # location of the mavenOS root file
addressMaven = 'C:/Users/holtb/Desktop/mavenOS/' + ID + '.txt' # location of maven's profile 

def displayProfile(ID):
	content = admin.upload(root, ID)
	for i in content:
		print(i[0], ':', i[1])
	return

def sourceNetwork(ID):
	content = []
	anchor = admin.upload(root, ID)
	for i in anchor:
		if i[0] == 'connection':
			content.append(i[1])
	return content

def sourceAttributesLibrary(ID):
	content = []
	anchorBranch = []
	anchorRoot = admin.upload(root, ID)
	for i in anchorRoot:
		if i[0] not in content:
			content.append(i[0])
		if i[0] == 'connection':
			anchorBranch.append(i[1])
	for i in anchorBranch:
		node = admin.upload(root, i)
		for i in node:
			if i[0] not in content:
				content.append(i[0])
	return content

def sourceNodes(id, qualifier):
	content = []
	anchorBranch = []
	anchorRoot = admin.upload(root, ID)
	for i in anchorRoot:
		if i[0] == 'connection':
			anchorBranch.append(i[1])
	for i in anchorBranch:
		node = admin.upload(root, i)
		for i in node:
			if i[0] == 'type' and i[1] == qualifier:
				content.append(node[0][1])
	return content

displayProfile(ID)
importCall = 'n' # input('Import new data? (Enter nodeID or "n"): ')
if importCall != 'n':
	data = admin.importCreate(root, importCall)
	nodeUpdate = analyst.locationsBasic(data)
	for i in nodeUpdate:
		admin.nodeUpdate(importCall, i)
admin.exportCreate(root, str(datetime.date.today()) + '_' + ID + '_sourceNetwork', sourceNetwork(ID))
admin.exportCreate(root, str(datetime.date.today()) + '_' + ID + '_sourceAttributesLibrary', sourceAttributesLibrary(ID))
admin.exportCreate(root, str(datetime.date.today()) + '_' + ID + '_sourceJobs', sourceNodes(ID, 'job'))
input()
