# Creates a new Mark and Maven network node

import random
import csv
import string
import admin

profile = [
	['id', admin.idCreate()],
	['connection', '1SKSZ1JLB5YNR9'],
	['connection', 'IJPM2AAHJR4YXN']
	]
admin.nodeCreate(profile)
admin.nodeUpdate('1SKSZ1JLB5YNR9', ['connection', profile[0][1]])
admin.nodeUpdate('IJPM2AAHJR4YXN', ['connection', profile[0][1]])