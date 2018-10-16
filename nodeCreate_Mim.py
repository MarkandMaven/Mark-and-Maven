# Creates a new Mark and Maven network node

import random
import csv
import string
import admin

profile = [
	['id', admin.idCreate()],
	['connection', '3KKX1Q5C9FE0AV']
	] #generateID
admin.nodeCreate(profile)
admin.nodeUpdate('3KKX1Q5C9FE0AV', ['connection', profile[0][1]])