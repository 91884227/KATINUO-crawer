#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[1]:


import time, re
from bs4 import BeautifulSoup
from tqdm import tqdm
import numpy as np
import itertools
import pandas as pd
import sys
import warnings
import requests
warnings.filterwarnings("ignore")
import multiprocessing as mp


# # find max page

# In[ ]:


class board_crawer:
    def __init__(self, board_ = 3867, constrain_ = True):
        self.board = board_
        self.my_headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}
        
        print("start to get data from %d BOARD" % self.board)
        print("find max page of %d board" % self.board)
        self.get_max_page(constrain_)
        
        print("create url list")
        temp = "https://ck101.com/forum-%d-" % self.board
        list_URL = [temp + "%d.html" % i for i in np.arange(1, self.MAX_page+1)]
        
        print("start to get all the block")
        buf = [ self.URL_find_block(i) for i in tqdm(list_URL)]
        
#         pool = mp.Pool(processes = 3)
#         pool.map(self.URL_find_block, tqdm(list_URL))
        
        list_block = list(itertools.chain(*buf))  

        print("start to get title and data from block")
        try:
            self.data = [ self.block_get_title_data(i) for i in list_block]
            print("success to get %d board data" % self.board)
        except:
            print("fail to get %d board data" % self.board)
        
    
    def get_max_page(self, constrain_):
        if( constrain_):
            self.MAX_page = 3
        else:
            try:
                #
                url =  "https://ck101.com/forum-%d-1.html" % self.board
                r = requests.get(url, headers = self.my_headers)
                soup =  BeautifulSoup(r.text)
                buf = soup.select(".pageNumber")[0].text
                self.MAX_page = int(buf.replace("\n",'').replace("/",''))
                print("Success to get Max page of %s: %d" % (url, self.MAX_page))
            except:
                print("fail to get Max page of %s" % url)
            
    def URL_find_block(self, URL_):
        buf = None
        try:
            #print(URL_)
            time.sleep(0.5)
            r = requests.get(URL_, headers = self.my_headers)
            soup = BeautifulSoup(r.text)
            buf = soup.select(".subject")
        except:
            print("error in block_get_title_data: %s" % URL_)

        return(buf)   
    
    def block_get_title_data(self, block_):
        buf_title = "block_get_title_data---error---"
        buf_date = "block_get_title_data---error---"
        try:
            buf_title = block_.select(".s.xst")[0]['title']
            buf_date = block_.select(".postInfo_dateline")[0].text
        except:
            print("error in block_get_title_data")
           # print(block_)

        return( (buf_title, buf_date, self.board) )    

