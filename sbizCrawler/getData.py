import requests
import pprint
import json

import pandas as pd

# Headers Query String Parameters
# admiCd: 지역코드
# upjongCd: G471903 (편의점)

simpleLoc = ''
admCd = ''
dataUrl = "https://sg.sbiz.or.kr/godo/getAvgAmtInfo.json"
popularUrl = "https://sg.sbiz.or.kr/godo/getPopularInfo.json"

lines = open('./admCd.txt','r')
for line in lines:
  (simpleLoc, admCd) = line.split(': ')
  if not 'NO' in admCd:
    admCd = line.split('_')[1]
  print(simpleLoc + " " + admCd)

payload = {'admiCd': 26230520, 'upjongCd': 'G471903', 'simpleLoc':'부산 부산진구 부전2동'}
r = requests.get(dataUrl, params=payload, verify=False)
print( r.status_code)
pprint.pprint(json.loads(r.text))
data = json.loads(r.text)
annualSales = data['annualSales'] # maxAmt: 최대매출, minAmt: 최소매출, saleAmt: 평균매출 (array)
guAmt = data['guAmt'] # 구 평균
guMax = data['guMax'] # 구 max
guMin = data['guMin'] # 구 min
prevMonCnt  = data['prevMonCnt']  # 이전달 선택업종 업소수
prevYearCnt = data['prevYearCnt'] # 이전년 선택업종 업소수
saleCnt     = data['saleCnt']     # 현재  선택업종 업소수

import datetime
def get_epochtime_ms():
  return round(datetime.datetime.utcnow().timestamp() * 1000)

payload = {'admiCd': 26230520, 'mililis': get_epochtime_ms()}
r = requests.get(popularUrl, params=payload, verify=False)
print( r.status_code)
pprint.pprint(json.loads(r.text))
data = (json.loads(r.text))["population"]