import webbrowser
import csv
import json
import itertools
import operator
import random
from geopy.geocoders import Nominatim

def most_common(data):
	print(data)
	sorted_list = sorted((x, i) for i, x in enumerate(data))
	groups = itertools.groupby(sorted_list, key=operator.itemgetter(0))
	def _auxfun(g):
		item, iterable = g
		count = 0
		min_index = len(data)
		for _, where in iterable:
			count += 1
			min_index = (min(min_index, where))
		return count, -min_index
	return max(groups, key=_auxfun)[0]

def locationsBasic(data):
	data_in_memory = []
	everywhere_tuples = []
	nighttimes_tuples = []
	workhour_tuples = []
	dates_captured = []

	for i in data[0]["bundle"]["rumpel/locations/ios"]:
		data_in_memory.append(i)
	for i in data_in_memory:
		if int(i['data']['dateCreatedLocal'][11:13]) < 6:
			nighttimes_tuples.append([i['data']['latitude'], i['data']['longitude']])
		if int(i['data']['dateCreatedLocal'][11:13]) > 8 and int(i['data']['dateCreatedLocal'][11:13]) < 19:
			workhour_tuples.append([i['data']['latitude'], i['data']['longitude']])
		dates_captured.append(i['data']['dateCreatedLocal'][0:10])
		everywhere_tuples.append([i['data']['latitude'], i['data']['longitude']])
	

	geolocator = Nominatim(user_agent="Mark_and_Maven")
	locationBigly = geolocator.reverse(str(most_common(everywhere_tuples)))
	locationBiglyAddress = locationBigly.address
	try: 
		locationBigNight = geolocator.reverse(str(most_common(nighttimes_tuples)))
		locationBigNightAddress = locationBigNight.address
	except ValueError:
		locationBigNightAddress = ''
		print('locationBigNight failed, possible nighttime data not found')
	locationBigWork = geolocator.reverse(str(most_common(workhour_tuples)))
	locationBigWorkAddress = locationBigWork.address

	locationsBasic = [
		['locationBigly', locationBiglyAddress],
		['locationBigNight', locationBigNightAddress],
		['locationBigWork', locationBigWorkAddress],
		]

	return locationsBasic