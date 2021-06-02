# -*- coding:utf-8 -*-

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import json
import pprint

URL = 'https://sg.sbiz.or.kr/'

# 행정동 list는 소상공인 시장분석 파일에서 가져왔습니다.
dong_list = ['부전2동', '기장읍', '우2동', '부전1동', '범일2동', '중1동', '정관읍', '우1동', '대연3동', '좌2동', '괘법동', '녹산동', '남천1동', '좌1동', '광복동', '하단2동', '범천1동', '전포1동', '민락동', '중앙동', '용호1동', '연산9동', '반여1동', '연산5동', '온천1동', '재송1동', '당리동', '명지동', '감전동', '남산동', '다대1동', '모라1동', '수민동', '안락2동', '남포동', '수영동', '화명3동', '연산4동', '광안2동', '명륜동', '구포1동', '온천3동', '하단1동', '덕천2동', '대연1동', '양정1동', '온천2동', '동삼1동', '구서2동', '부평동', '거제1동', '연산1동', '초량3동', '광안1동', '엄궁동', '장안읍', '장림2동', '일광면', '초읍동', '전포2동', '안락1동', '구서1동', '광안3동', '개금1동', '학장동', '망미1동', '명지1동', '대연5동', '대저2동', '남항동', '사직2동', '대저1동', '괴정3동', '구포2동', '장전1동', '반송1동', '괴정1동', '반송2동', '서3동', '신평1동', '재송2동', '가야1동', '연산2동', '당감1동', '사직1동', '부곡3동', '주례2동', '양정2동', '반여2동', '금곡동', '장전2동', '장림1동', '송정동', '만덕2동', '다대2동', '연산8동', '충무동', '사직3동', '남천2동', '용호3동', '명장1동', '수정2동', '광안4동', '용호2동',
             '좌4동', '개금3동', '연산6동', '감천1동', '화명1동', '중2동', '신평2동', '가야2동', '서대신1동', '암남동', '장전3동', '거제3동', '괴정4동', '덕천1동', '덕포2동', '부암1동', '구포3동', '거제2동', '금사동', '연지동', '청학2동', '복산동', '부암3동', '주례3동', '초량1동', '초량2동', '범일1동', '만덕3동', '대연4동', '문현3동', '봉래1동', '부곡2동', '영선1동', '보수동', '서2동', '화명2동', '당감4동', '우3동', '문현1동', '주례1동', '감만1동', '괴정2동', '강동동', '삼락동', '덕포1동', '용당동', '대연6동', '범천2동', '문현2동', '망미2동', '명장2동', '동대신3동', '대청동', '문현4동', '부민동', '부곡4동', '좌3동', '반여3동', '철마면', '청룡노포동', '좌천동', '구평동', '우암동', '부곡1동', '명지2동', '영선2동', '만덕1동', '동광동', '서대신3동', '영주1동', '동대신2동', '용호4동', '청학1동', '연산3동', '동삼2동', '선두구동', '당감2동', '가덕도동', '서1동', '덕천3동', '감천2동', '남부민1동', '동대신1동', '반여4동', '남부민2동', '가락동', '거제4동', '개금2동', '서대신4동', '아미동', '감만2동', '초량6동', '수정1동', '동삼3동', '영주2동', '신선동', '금성동', '수정4동', '범일5동', '봉래2동', '모라3동', '수정5동', '금사회동동', '초장동']

capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+

driver = webdriver.Chrome(executable_path='./chromedriver',
                          desired_capabilities=capabilities,)
driver.get(url=URL)


def removePopup():
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'close'))
        )
        check_btn = driver.find_element_by_xpath(
          '//*[@id="help_guide"]/div/div[2]/div[1]/label'
        )
        check_btn.click()
        close_btn = driver.find_element_by_xpath(
          '//*[@id="help_guide"]/div/div[2]/a')
        close_btn.click()
    finally:
        pass
        # driver.quit()

def searchDong(dong):
    try:
      WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, 'searchAddress'))
      )
      search_box = driver.find_element_by_xpath('//*[@id="searchAddress"]')
      search_box.clear()
      search_box.send_keys(dong)
      driver.find_element_by_xpath('//*[@id="layerPopAddressMove"]').click()
    finally:
        pass


def getIdPw():
  f = open("idpw.txt", 'r')
  ans = []
  for line in f:
    line = line.strip()
    ans.append(line)
  return ans

def login():
  driver.find_element_by_xpath('//*[@id="header"]/div/ul/li[3]/div/a').click()
  try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn_login'))
    )
    (id, pw) = getIdPw()
    driver.find_element_by_id('id').send_keys(id)
    driver.find_element_by_id('pass').send_keys(pw)
    driver.find_element_by_class_name('btn_login').click()
    time.sleep(5)
  # except:
  #   driver.quit()
  finally:
    pass

def detailAnalysis():
  driver.find_element_by_xpath('//*[@id="toLink"]/a').click()
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="upjong"]/ul/li[3]/label').click()
  time.sleep(0.5)
  input_tag = driver.find_element_by_xpath('//*[@id="viewlist_check_best_1"]')
  input_tag.find_element_by_xpath("../label").click()
                                
  time.sleep(0.5)
  driver.find_element_by_xpath('//*[@id="checkTypeConfirm"]').click()
  time.sleep(1.5)
  
def getAnswer(dong):
  driver.find_element_by_xpath('//*[@id="map"]/div[1]/div/div[6]/div[2]/div/ul/li[4]').click()
  driver.find_element_by_xpath('//*[@id="map"]/div[1]/div/div[6]/div[3]/img').click()
  try:
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.ID, '1-1'))
    )
    span = driver.find_element_by_xpath('//*[@id="reportCont"]/div[15]/div[2]/strong/span')
    spanText = span.text
    print("{}:{}".format(dong, spanText))
    print("{}:{}".format(dong, spanText), file=out)
    driver.find_element_by_xpath('//*[@id="bind"]/div/a').click()
    time.sleep(2)
  # except:
    # driver.quit()
  finally:
    pass

if __name__ == "__main__":
    # 팝업 제거
    removePopup()
    login()
    detailAnalysis()
    # print(driver.find_element_by_xpath('//*[@id="data_pop"]/div[2]/a/h4').text)
    with open("answer.txt", "wt") as out:
      for dong in dong_list:
          print(dong)
          searchDong("부산 " + dong)
          time.sleep(1)
          dong = dong.replace(" ", "")
          getAnswer(dong)

driver.close()
