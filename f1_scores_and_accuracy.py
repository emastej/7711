#@author: emastej
#Instructions:Simulate the effect of rare events on accuracy and F-measure: 
#Write a program that shows how the accuracy and F-measure change if you keep 
#the number of TP, FP, and FN constant, but increase the number of TNs. 
#So, the x-axis will be the count of TNs, and the y-axis will show accuracy and 
#F-measure. (Hint: sketch out what you expect this to look like.)

#accuracy = (TP + TN) / (TP + TN + FP + FN)

#Precision = TP/ (TP + FP)
#Recall = TP/ (TP + FN)
#F-measure = 2*Precision *Recall / (Precision + Recall)

import matplotlib.pyplot as plt
TN_list = []
F1_list = []
acc_list = []

#Initial constants for TP, FP, and FN.  
#Change constants to see how graph is affected
TP = 1
FP= 1
FN= 1

for x in range (0,50):
    TN = x
    
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
plt.xlabel('Number of True Negatives')
plt.legend(loc='lower right')
plt.show()
    

    
    