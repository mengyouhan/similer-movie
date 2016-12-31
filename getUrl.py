from selenium import webdriver
import os,time


url = 'https://movie.douban.com/subject_search?search_text={}'.format()
driver = webdriver.Chrome()
driver.get(url)
# driver.find_element_by_css_selector("#inp-query").click()
driver.find_element_by_css_selector("#inp-query").send_keys('命运')
time.sleep(5)
driver.find_element_by_css_selector(".inp-btn").click()