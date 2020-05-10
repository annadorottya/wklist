# -*- coding: utf-8 -*-

import requests
import json
from collections import defaultdict
import argparse
import time

parser = argparse.ArgumentParser(description='List WaniKani kanjis by levels and waves.')

args = parser.parse_args()

file = open("api2_key","r")
api2_key = file.read()
file.close()

headers = {'Authorization': 'Bearer ' + api2_key}

first_wave = defaultdict(str)
second_wave = defaultdict(str)
shortlevels = []

url = "https://api.wanikani.com/v2/subjects/"
while True:
	r = requests.get(url, headers=headers)
	data=r.json()
	for i in data["data"]:
		ids = ""
		print(i["id"],i["object"])
	url = data['pages']['next_url']


#1-439, 8761-8799, 8819-8833, 8856-8857: radical
#440-2466, 8834-8840, 8858-8864, 8880-8886: kanji
#2467-8760, 8800-8818, 8841-8855, 8865-8879, 8887-8905: vocab
