#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from tqdm import tqdm


# In[3]:


book_df = pd.read_csv('Quills_and_goodreads_db.csv')


# In[4]:


def get_info_book_picks():    
    book_picks = ["1984'","Alchemist", "Wintercraft"]
    book_picks_df_list = []
    book_picks_df = pd.DataFrame(columns=book_df.columns)
    for i,book in enumerate(book_picks):
        book_picks_df_list.append(book_df.loc[book_df['Title']==book].drop_duplicates(subset='Title'))
    book_picks_df = book_picks_df.append(book_picks_df_list)    
    return book_picks_df


# In[6]:


def display_table():
    display_df = book_df.drop('Description', axis=1,inplace=False)
    for i in display_df.index:
        display_df['Title'].iloc[i] = " ".join(display_df['Title'].iloc[i].split("+")) 
    return display_df


# In[ ]:




