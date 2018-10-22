# Creates a new Mark and Maven network node

import random
import csv
import string
import admin

profile = [
	['id', admin.idCreate()],
	['connection', 'IDK2JJSBMTCO8E'],
	['connection', 'IJPM2AAHJR4YXN']
	]
admin.nodeCreate(profile)
admin.nodeUpdate('IDK2JJSBMTCO8E', ['connection', profile[0][1]])
admin.nodeUpdate('IJPM2AAHJR4YXN', ['connection', profile[0][1]])