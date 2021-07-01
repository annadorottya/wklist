# -*- coding: utf-8 -*-

import requests
import json
import argparse
import time

parser = argparse.ArgumentParser(description='List WaniKani kanjis by levels and waves.')

args = parser.parse_args()

file = open("api2_key","r")
api2_key = file.read()
file.close()

headers = {'Authorization': 'Bearer ' + api2_key}

first_wave = {}
second_wave = {}
shortlevels = []

for l in range(1,61):
	time.sleep(1)
	first_wave[l] = ""
	second_wave[l] = ""
	radicalids = []
	r = requests.get("https://api.wanikani.com/v2/subjects/?types=radical&levels=" + str(l), headers=headers)
	data=r.json()
	for i in data["data"]:
		radicalids.append(i['id'])

	r = requests.get("https://api.wanikani.com/v2/subjects/?types=kanji&levels=" + str(l), headers=headers)
	data=r.json()
	for i in data["data"]:
		if set(i["data"]["component_subject_ids"]).intersection(radicalids):
			second_wave[l] += i["data"]["characters"]
		else:
			first_wave[l] += i["data"]["characters"]
	print("Level " + str(l) + " 1st wave: " + first_wave[l] + " (total count: " + str(len(first_wave[l])) + ")")
	print("Level " + str(l) + " 2nd wave: " + second_wave[l] + " (total count: " + str(len(second_wave[l])) + ")")	
	if len(first_wave[l]) >= (len(first_wave[l]) + len(second_wave[l]))*0.9:
		print("Level " + str(l) + " is a short level!")
		shortlevels.append(l)
print("Short levels are: " + str(shortlevels))
