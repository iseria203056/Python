#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests as rq
import time
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# In[2]:


x=input()
stock=[]
while x!="end":
    stock.append(x)
    x=input()


# In[ ]:


while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    for code in stock:
        url =  "https://finance.yahoo.com/quote/"+code    
        response = rq.get(url) 
        html_doc = response.text # text 屬性就是 html 檔案
        soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
        print(code+"  price="+soup.find("span",class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").string)
    time.sleep(30)
    cls()


# In[5]:




