# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
# SAMPLE USAGE:
# python3 Agreement_Calculating.py labels1.csv labels2.csv

import sys
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import f1_score

def creating_list(number): #expects the number of argument for sys.argv
    lst = []
    for el in open(sys.argv[number]).read():
        lst.append(el.strip('\n'))
    return [e for e in lst if e != ""]

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print('Wrong number of arguments. The number of given arguments must be two.')
    
    else:
        labels1 = creating_list(1)
        labels2 = creating_list(2)

        print("Cohen\'s kappa score for the given lists is", cohen_kappa_score(labels1, labels2))
        print("F1 score for majority class is", f1_score(labels1, labels2, average = None)[0])
        print("F1 score for minority class is", f1_score(labels1, labels2, average = None)[1])
        



