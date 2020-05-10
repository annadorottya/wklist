# -*- coding: utf-8 -*-

#import requests
import json
from collections import defaultdict
import argparse
import re

parser = argparse.ArgumentParser(description='Create kanji list from a given text.')
parser.add_argument('text', metavar='T', type=str, nargs='?', help='Text you want to convert to list.')
args = parser.parse_args()

if args.text == None:
	text = u"単語集第一章佐藤家一日家族構成氏大手製造会社勤務海外事業部課長夫人長女中学校小学校長男住宅分譲集合住宅都心電車程度郊外6時起床始まる勤め先以上住む毎日起きる普通奥さん夫子供朝食準備7時ご飯味噌汁野菜煮しめ漬物和食食べる目玉焼き洋食飲む日本茶違う最近一般的手間多新聞昨日知識仕入れる天気予報日課終わる会社学校出かける特に大都市地下鉄乗車率"
else:
	text = args.text

text = ''.join(set(re.sub(u"[a-zA-Z\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f*]", '', text)))

print(text)