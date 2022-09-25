import openpyxl
import requests
from bs4 import BeautifulSoup

fpath = r'/home/sorang/coding/Python_Excel/참가자_data.xlsx'

wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트 선택

codes = [
    '047810',
    '000660',
    '005930'
]

row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    print(price)
    ws[f'B{row}'] = int(price)
    row += 1

wb.save(fpath)
