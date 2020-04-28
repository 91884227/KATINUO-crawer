#!/usr/bin/env python
# coding: utf-8

# # import tool

# In[5]:


import time, re
from bs4 import BeautifulSoup
from tqdm import tqdm
import numpy as np
import itertools
import pandas as pd
import sys
import warnings
warnings.filterwarnings("ignore")
import multiprocessing as mp
import requests


# # import self-define data

# In[6]:


from module.board_crawer_class import board_crawer


# In[7]:


def crawer_map_func(number_):
    board_class = board_crawer(board_ = number_,
                               constrain_ = bool(sys.argv[1]))
    return( board_class.data)


# In[8]:


def output_data(buf_):
    df = pd.DataFrame(buf_)
    df.columns = ["title", "date", "board"]
    # delete some data
    df = df[df['title'] != "block_get_title_data---error---" ]
    df = df[df['date'] != "block_get_title_data---error---" ]
    name = "katino_data.csv"
    df.to_csv(name, index = False, encoding= 'UTF-8')


# In[9]:


if __name__ == "__main__": 
    print("check legal_index exist...")
    page_data = pd.read_csv("legal_index_kuru.csv")
    legal_page = page_data["page_number"].to_numpy()
    
    print("start to get data...")
    pool = mp.Pool(processes = int(sys.argv[2]))
    buf = pool.map(crawer_map_func, tqdm(legal_page))
    buf_flatten = list(itertools.chain(*buf))
    
    try: 
        output_data(buf_flatten)
        print("sucuess to crawl data: %s" % "katino_data.csv")
    except:
        print("fail to crawl data")


# In[ ]:




