import requests
from bs4 import BeautifulSoup

base_url = "https://search.shopping.naver.com/search/all?query="
keyword = '휴대폰 거치대'

search_url = base_url + keyword

r = requests.get(search_url)

soup = BeautifulSoup(r.text, "html.parser")
items = soup.select_one('.adProduct_depth__s_IUT') # 카테고리 전체 클래스 
item_list = items.select(".adProduct_category__ZIAfP.adProduct_nohover__zHCEV") # 세부 카테고리 클래스

cate_list = []

item_list_len = len(item_list)

cate_list.append(keyword)
for i in range(item_list_len):
    cate_list.append(item_list[i].text)
if item_list_len == 3:
    cate_list.append('')
    
print(cate_list)