#!/usr/bin/env python
# coding: utf-8

import pandas as pd

book_df = pd.read_csv('Quills_and_goodreads_db.csv')

def get_info_book_picks():    
    book_picks = ["1984'","Alchemist", "Wintercraft"]
    book_picks_df_list = []
    book_picks_df = pd.DataFrame(columns=book_df.columns)
    for i,book in enumerate(book_picks):
        book_picks_df_list.append(book_df.loc[book_df['Title']==book].drop_duplicates(subset='Title'))
    book_picks_df = book_picks_df.append(book_picks_df_list)    
    return book_picks_df


def create_table():
    create_df = book_df.drop('Description', axis=1,inplace=False)
    for i in create_df.index:
        create_df['Title'].iloc[i] = " ".join(create_df['Title'].iloc[i].split("+")) 
    create_df.to_csv("book_author_rating.csv")    

def display_table():
    display_df = pd.read_csv('book_author_rating.csv')
    return display_df