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
import admin

ID = 'IJPM2AAHJR4YXN' # maven's ID number
root = 'C:/Users/holtb/Desktop/mavenOS/' # location of the mavenOS root file
addressMaven = 'C:/Users/holtb/Desktop/mavenOS/' + ID + '.txt' # location of maven's profile 

def displayProfile(ID):
	content = admin.upload(ID)
	for i in content:
		print(i[0], ':', i[1])
	return

def sourceNetwork(ID):
	content = []
	anchor = admin.upload(ID)
	for i in anchor:
		if i[0] == 'connection':
			content.append(i[1])
	return content

def sourceAttributesLibrary(ID):
	content = []
	anchorBranch = []
	anchorRoot = admin.upload(ID)
	for i in anchorRoot:
		if i[0] == 'connection':
			anchorBranch.append(i[1])
	for i in anchorBranch:
		node = admin.upload(i)
		for i in node:
			if i[0] not in content:
				content.append(i[0])
	return content

def sourceNodes(id, qualifier):
	content = []
	anchorBranch = []
	anchorRoot = admin.upload(ID)
	for i in anchorRoot:
		if i[0] == 'connection':
			anchorBranch.append(i[1])
	for i in anchorBranch:
		node = admin.upload(i)
		for i in node:
			if i[0] == 'type' and i[1] == qualifier:
				content.append(node[0][1])
	return content

displayProfile(ID)
admin.exportCreate(str(datetime.date.today()) + '_' + ID + '_sourceNetwork', sourceNetwork(ID))
admin.exportCreate(str(datetime.date.today()) + '_' + ID + '_sourceAttributesLibrary', sourceAttributesLibrary(ID))
admin.exportCreate(str(datetime.date.today()) + '_' + ID + '_sourceJobs', sourceNodes(ID, 'job'))
input()

'''
-—
0.6 features
An admin user can create nodes for candidates
AAUC see a list of candidates by job posting
AAUC see a list of all active candidates

——
-—
A user can search a Mark and Maven job board

——
-—
A user can create a dossier
A user’s dossier is very badass in comparison to  resume
A user can see how their dossier stacks up against other dossiers
A user can see how qualified they’d be for the jobs they want to poly for using their dossier
A user can customize their dossier to each role they want to apply for

——
-—
A user can apply to jobs with their dossier

——
'''