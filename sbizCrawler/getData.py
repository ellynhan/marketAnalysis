import requests
import pprint
import json

# Headers Query String Parameters
# admiCd: 지역코드
# upjongCd: G471903 (편의점)

url = "https://sg.sbiz.or.kr/godo/getAvgAmtInfo.json"

payload = {'admiCd': '26230520', 'upjongCd': 'G471903', 'simpleLoc':'부산 부산진구 부전2동'}
r = requests.get(url, params=payload, verify=False)
print( r.status_code)
pprint.pprint(json.loads(r.text))
# session = requests.Session()
# session.get(url)
# print(session.cookies.get_dict())