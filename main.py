#imports
import numpy as np
import pandas as pd
import os
import re
import argparse


#Import Clean df and summary tables
df = pd.read_csv('Output/cleanIMDB.csv',encoding = 'latin-1')

dacade_table = pd.read_csv('Output/decade_table.csv',encoding = 'latin-1')

score_table = pd.read_csv('Output/score_table.csv',encoding = 'latin-1')

country_table = pd.read_csv('Output/country_table.csv',encoding = 'latin-1')

df_str =df.astype('str')

#Creating filtering tool 
parser = argparse.ArgumentParser(description='Movie filter')
parser.add_argument('-t','--typesearch', type=str, metavar='', help='Type of search(Input: title, year, director, genre, etc.)')
parser.add_argument('-m','--match', type=str, metavar='',  help='Type of search must match characters(Input: hobbit, 2016, Peter Jackson, Action, etc)')
#group = parser.add_mutually_exclusive_group()
#group-add_argument(
#group-add_argument(

#No he conseguido que funcione el add_mutually_exclusive_group.

args=parser.parse_args()

def filtro(typesearch,match):
    selection = df_str[df_str[typesearch].str.contains(match,case=False)]
    return selection

if __name__ == '__main__':
    if args.typesearch != None and args.match != None:
       print(filtro(args.typesearch, args.match))
    else:
       print('You need to enter the parameters -t for the type of search and -m for the character look up')
    