#!/usr/bin/env python
# coding: utf-8

#  # import tool

# In[12]:


from selenium import webdriver
import time, re
from bs4 import BeautifulSoup
from tqdm import tqdm
import numpy as np
import itertools
import pandas as pd
import sys
import warnings
warnings.filterwarnings("ignore")


# In[67]:


def find_information(block_):
    return_buf = (-1, 0)
    try:
        tag = block_.text.replace("\n", "")
        page_number = int(block_.attrs["href"].replace("/forum-", "").replace("-1.html", ""))
        return_buf = (page_number, tag)
    except:
        print("error happand")
    return( return_buf)


# In[ ]:


if __name__ == '__main__':
    #DRIVER_PATH = "C:/Users/Chuck/Desktop/計畫/chromedriver.exe"
    DRIVER_PATH = str(sys.argv[1])
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get("https://ck101.com/forum-3590-1.html")
    soup =  BeautifulSoup(driver.page_source)
    driver.close()
    all_block = soup.select(".channel_menu.sticky_position_with_15")[0].find_all("a")
    
    buf = [find_information(i) for i in all_block]
    df = pd.DataFrame(buf)
    df.columns = ["page_number", "board_name"]
    df = df[df["page_number"] > 0]
    name = "legal_index_kuru.csv"
    df.to_csv(name, index = False, encoding= 'UTF-8')
    print("success to generate the file %s " % name )
    


# In[13]:


# DRIVER_PATH = "C:/Users/Chuck/Desktop/計畫/chromedriver.exe"

# driver = webdriver.Chrome(DRIVER_PATH)
# driver.get("https://ck101.com/forum-3590-1.html")

# soup =  BeautifulSoup(driver.page_source)
# driver.close()

# all_block = soup.select(".channel_menu.sticky_position_with_15")[0].find_all("a")

# buf = [find_information(i) for i in all_block]

# df = pd.DataFrame(buf)
# df.columns = ["page_number", "board_name"]
# df = df[df["page_number"] > 0]
# df.to_csv(name, index = False, encoding= 'UTF-8')
# print("success to generate the file %s " % name )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




