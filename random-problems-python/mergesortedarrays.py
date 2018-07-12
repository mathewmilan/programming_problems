'''
Created on Oct 27, 2017

@author: butterflyeffect
'''
from __builtin__ import raw_input

#Merge two sorted arrays
def merge (a, b):
    i = 0; j = 0; c = []
    while (i < len(a) and j < len(b)):
        if (a[i] < b[j]):
            c.append(a[i])
            i += 1
        elif (a[i] == b[j]):
            c.append(a[i])
            c.append(b[j])
            i += 1
            j += 1
        else:
            c.append(b[j])
            j += 1
    while (i < len(a)):
        c.append(a[i])
        i += 1
    while (j < len(b)):
        c.append(b[j])
        j += 1
    for e in c:
        print (e) 

a = [int(e) for e in raw_input().split(' ')]
b = [int(e) for e in raw_input().split(' ')]

merge(a, b)