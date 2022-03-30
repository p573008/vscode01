# step1.라이브러리 불러오기
import requests
from bs4 import BeautifulSoup as bs
#import telegram
import time
import pandas as pd

# step2.제품명과 제품가격정보를 담을 빈 리스트 선언
product_name = []
product_price = []

# step3.for문을 이용해서 원하는 페이지에 접근, 정보 추출 후 리스트에 담기
for page_num in range(3):
    # range를 이용하면 0부터 인덱스가 시작되므로 page_num에 1을 더해준 url을 이용
    url = f'https://smartstore.naver.com/compuzone/category/ALL?st=RECENT&free=false&dt=IMAGE&page={page_num+1}&size=40'
    
    # html 정보 받아와서 파싱
    response = requests.get(url)
    soup = bs(response.text , 'html.parser')

    # css selector로 페이지 내의 원하는 정보 가져오기
    html_product = soup.select('strong.QNNliuiAk3')
    html_price = soup.select('span.nIAdxeTzhx')

    # 텍스트만 추출
    for i in html_product:
        product_name.append(i.get_text())
        
    for i in html_price:
        product_price.append(i.get_text())

# step4.zip 모듈을 이용해서 list를 묶어주기        
list_sum = list(zip(product_name, product_price))


# step5.데이터프레임의 첫행에 들어갈 컬럼명
col = ['제품명','가격']

# step6.pandas 데이터 프레임 형태로 가공
df = pd.DataFrame(list_sum, columns=col)

# step7.엑셀에 저장
df.to_excel('컴퓨존 제품 목록.xlsx')