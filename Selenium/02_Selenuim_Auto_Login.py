from sys import implementation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동 로그인 페이지
driver.implicitly_wait(5) # 웹페이지가 로딩될 때까지 5초는 기다림
# driver.maximize_window() # 화면 최대화
driver.get(" https://gbehcm.eduro.go.kr/")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#lusername") # 태그 자동으로 선택
id.click()
pyperclip.copy("eksajrm0624")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#lpassword") # 태그 자동으로 선택
pw.click()
pyperclip.copy("Dltkdals1!")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "body > div > div.login > form > div > button")
login_btn.click()

def imple():
    Rstudio = "Script RConsole History"
    
    return 0
    
    import beautiful soup
    unoirt