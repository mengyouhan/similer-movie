from selenium import webdriver
import os,time,re
from bs4 import BeautifulSoup
import requests,cs1

class SearchUrl(object):
    def __init__(self,searchM):
        self.searchM = searchM
    def start(self):
        # searchM = '命运石之门'
        url = 'https://movie.douban.com/subject_search?search_text={}'.format(self.searchM)

        wb_data = requests.get(url)

        soup = BeautifulSoup(wb_data.text, 'lxml')
        titles = soup.select('#wrapper .article  .pl2 a')
        data = [x['href'] for x in titles]
        data2 = [re.sub('[ \r\n]', '', x.get_text()) for x in titles]
        return data[0]





# driver = webdriver.Chrome()
# driver.get(url)
# driver.find_element_by_css_selector("#inp-query").click()
# driver.find_element_by_css_selector("#inp-query").send_keys('命运')
# time.sleep(5)
# driver.find_element_by_css_selector(".inp-btn").click()