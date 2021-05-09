from os import remove
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time
import pprint

URL = 'https://sg.sbiz.or.kr'

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(executable_path='./chromedriver', desired_capabilities=caps)
driver.get(url=URL)

close_btn = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH , '//*[@id="help_guide"]/div/div[2]/a'))
)

close_btn.click()

def process_browser_logs_for_network_events(logs):
    for entry in logs:
        log = json.loads(entry["message"])["message"]
        if (
            "Network.response" in log["method"]
            or "Network.request" in log["method"]
            or "Network.webSocket" in log["method"]
        ):
            yield log


search_box = driver.find_element_by_xpath('//*[@id="searchAddress"]')
search_box.send_keys('장전 1동')

driver.find_element_by_xpath('//*[@id="layerPopAddressMove"]').click()
# search_val = WebDriverWait(driver, 100).until(
#     EC.presence_of_element_located((By.XPATH , '//*[@id="search-view1_0"]'))
# )
# search_val.click()
# driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[3]/div[3]/a[2]').click()

logs = driver.get_log("performance")
events = process_browser_logs_for_network_events(logs)
with open("log_entries.json", "wt") as out:
    for event in events:
        pprint.pprint(event['params'], stream=out)
        # if 'response' in event['params']:
        #   pprint.pprint(event['params']['response'])
        # if 'documentURL' in event['params']:
        # #   if event['params']['documentURL'] == 'https://sg.sbiz.or.kr/godo/getAdmiInfo.json':
        #     pprint.pprint(event['params'])
# time.sleep(100)