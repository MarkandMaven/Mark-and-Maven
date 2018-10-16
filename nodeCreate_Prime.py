# Creates a new Mark and Maven network node

import random
import csv
import string
import admin

profile = [
	['id', admin.idCreate()],
	['connection', 'IJPM2AAHJR4YXN']
	] #generateID
admin.nodeCreate(profile)
admin.nodeUpdate('IJPM2AAHJR4YXN', ['connection', profile[0][1]])