# -*- coding: utf-8 -*-
"""
Created on Sat Sep 01 12:49:04 2018

@author: emastej
"""

#not sure what numbers to start with because if we are increasing TN, the pop 
#will increase too.  

#I will start with a group of 1000.  
#Sensitivity = .95, Spec can't do because TN changes
#I will run through rarity of 1%, 5%, and 10% of TP

#pop = 1000
#sen = .95


import matplotlib.pyplot as plt
TN_list = []
F1_list = []
acc_list = []

TP = 20
FP= 10
FN= 10

for x in range (5,25):
    TN = 10* x
    
    precision = TP/ float(TP + FP)
    recall = TP / float(TP +FN)

    F1 = (2*precision*recall) / float(precision + recall)

    accuracy = (TP + TN)/ float(TP + TN + FP + FN)
    
    TN_list.append(TN)
    F1_list.append(F1)
    acc_list.append(accuracy)

plt.figure
plt.plot(TN_list, F1_list, '-b', label = 'F score')
plt.plot(TN_list, acc_list, '-r', label= 'Accuracy')
plt.ylim(0,1)
plt.title('Accuracy and F score')
plt.xlabel('Number of False Negatives')
plt.legend(loc='right')
plt.show()
    
    
    