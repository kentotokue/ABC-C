'''
Created on 2021/11/13

@author: kentoo
'''
S = str(input())
R = 0
B = 0
for i in range(len(S)):
    if S[i] == "0":
        R += 1
    else:
        B += 1
print(min(B,R)*2)
        