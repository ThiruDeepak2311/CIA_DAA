import numpy as np

import random as rd 
chars = ['a','c','g','t']
a  = ""
b = ""
l = 16
a_ct = c_ct = g_ct = t_ct = 0

while len(a) < l:
    ch = rd.choice(chars)
    if ch=='a' and a_ct<4:
        a+=ch
        a_ct+=1
    elif ch=='c' and c_ct<4:
        a +=ch
        c_ct+=1
    elif ch=='g' and g_ct < 4:
        a +=ch 
        g_ct+=1
    elif ch == 't' and t_ct < 4:
        a +=ch
        t_ct+=1

a_ct = c_ct = g_ct = t_ct = 0

while len(b) < l:
    ch = rd.choice(chars)
    if ch=='a' and a_ct<4:
        b+=ch
        a_ct+=1
    elif ch=='c' and c_ct<4:
        b+=ch
        c_ct+=1
    elif ch=='g' and g_ct < 4:
        b+=ch 
        g_ct+=1
    elif ch == 't' and t_ct < 4:
        b+=ch
        t_ct+=1
print(a)
print(b)
cols = len(b)
rows = len(a)
score = 5
penalty = -4
cols = len(b)
rows = len(a)
arr = np.zeros((rows+1, cols+1), dtype=int)

i=1 #row
j=1 #col 

def align(arr,i,j):
    if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1]+score
    else:
            m = max(arr[i-1][j-1], arr[i-1][j], arr[i][j-1])
            arr[i][j] = m + penalty  
    if j!=len(b):
        return align(arr,i,j+1)
    elif i==len(a):
        print(arr)
    else:
        j=1
        return align(arr,i+1,j)
        
align(arr,i,j)
