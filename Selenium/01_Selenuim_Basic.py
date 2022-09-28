from selenium import webdriver

fpath = '/home/sorang/chromedriver'

browser = webdriver.Chrome(fpath)

browser.get('https://www.naver.com')