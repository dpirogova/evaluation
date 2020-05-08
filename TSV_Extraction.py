#!/usr/bin/env python
# coding: utf-8

# SAMPLE USAGE:
# python3 TSV_Extraction.py file.tsv output.txt

import csv
import pandas as pd
import sys

tsv_doc = sys.argv[1]

def creating_lst(path): 
    with open(path, encoding='utf-8') as csvfile:
        k_reader = pd.read_csv(csvfile, sep='\t', comment='#', 
                                   skip_blank_lines=True, quoting=csv.QUOTE_NONE, header = None)
    return k_reader


file = creating_lst(tsv_doc)


def labeling_lines(my_df): #extracting lines and their metaphor labels from the tsv file
    
    num_rows = my_df.shape[0]
    sents = []
    curr_sent = ''
    metaphor = False
    curr_index = int(my_df[0][0].split( '-' )[0])
    last_char_index = int( my_df[1][0].split( '-' )[0] )

    for i in range(0, num_rows):
        if my_df[3][i] != '_' or my_df[4][i] != '_' or my_df[5][i] != '_' or my_df[6][i] != '_':
            metaphor = True
        sent_index = int(my_df[0][i].split('-')[0])
        first_char_index = int(my_df[1][i].split('-')[0])
        whitespaces = first_char_index - last_char_index 
        if whitespaces > 1 or sent_index != curr_index:
            curr_index = sent_index
            if metaphor == True:
                sents.append((curr_sent, 1))
            else:
                sents.append((curr_sent, 0))
            curr_sent = ''
            last_char_index = 0
            metaphor = False
            whitespaces = 0
        curr_sent = curr_sent + (" " * whitespaces) + my_df[2][i]
        last_char_index = int(my_df[1][i].split('-')[1])
    if metaphor == True:
        sents.append((curr_sent, 1))
    else:
        sents.append((curr_sent, 0))
    
    return sents

#creating the output txt
txt_file = open(sys.argv[2], "w")
for ln in labeling_lines(file):
    txt_file.write(str(ln) + '\n')
txt_file.close()
