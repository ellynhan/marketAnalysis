import requests
res = requests.get('https://sg.sbiz.or.kr/godo/index.sg#')
print(res.text)