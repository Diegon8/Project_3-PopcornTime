#imports
import numpy as np
import pandas as pd
import os
import re
import argparse


#Import Clean df and summary tables
df = pd.read_csv('Input/cleanIMDB.csv',encoding = 'latin-1')

dacade_table = pd.read_csv('Input/decade_table.csv',encoding = 'latin-1')

score_table = pd.read_csv('Input/score_table.csv',encoding = 'latin-1')

country_table = pd.read_csv('Input/country_table.csv',encoding = 'latin-1')

df_str =df.astype('str')

#Creating filtering tool 
parser = argparse.ArgumentParser(description='Movie filter')
parser.add_argument('-t','--typesearch', type=str, metavar='', help='Type of search(Input: title, year, director, genre, etc.')
parser.add_argument('-m','--match', type=str, metavar='', help='Type of search must match characters(Input: hobbit, 2016, Peter Jackson, Action, etc')

args=parser.parse_args()

def filtro(typesearch,match):
    return df_str[df_str[typesearch].str.contains(match,case=False)]

if __name__ == '__main__':
    print(filtro(args.typesearch, args.match))
    