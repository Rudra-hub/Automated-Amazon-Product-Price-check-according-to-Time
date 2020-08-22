import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
headers={"User-Agent":"Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
"""My personal Chrome Useragent id"""
rsponse=requests.get("https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i7/dp/B081JWZQJB/ref=sr_1_2?crid=2DX4TJQOXQ8P9&dchild=1&keywords=macbook+pro+2020&qid=1598100142&sprefix=mac%2Caps%2C544&sr=8-2",headers=headers)
                    #Getting response form choosen Amazon Product's URL & here requests.get is an Object
soup=BeautifulSoup(rsponse.content,"html.parser")
                   #rsponse.content is the Object of BeautifulSoup & by this html.parser we get html format data only by scraping
def price_check():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")    #getting current time
    print("Time: ", current_time)
    title = soup.find(id="productTitle").get_text()    #Scraping of Product Title & here productTitle is a tag
    price = soup.find(id="priceblock_ourprice").get_text().strip()   #.get_text() is getting o/p in text format
    print("Product name & specs:",title.strip())
    print("Product cost",price)
price_check()
while True:    #Running the above process repeatedly using delay
	price_check()
	print("Will fetch again after 10 seconds. automatically")
	time.sleep(10)