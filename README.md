# EM7711-hmwk1
Written in Python 2.7

Required Packages: matplotlib.pyplot 

Hmwk Instructions:
1. Simulate the effect of rare events on accuracy and F-measure: Write a program that shows how the accuracy and F-measure change if you keep the number of TP, FP, and FN constant, but increase the number of TNs. So, the x-axis will be the count of TNs, and the y-axis will show accuracy and F-measure. (Hint: sketch out what you expect this to look like.)

2. Check your work into GitHub, including your graph.

3. Check out a classmate’s code and run it. Write down everything that you had to fix to get it to run and produce output for you.

Equations:
Precision = TP/ (TP + FP)
Recall = TP/ (TP + FN)
F-measure = 2*Precision *Recall / (Precision + Recall)
Accuracy = (TP + TN) / (TP + TN + FP + FN)
