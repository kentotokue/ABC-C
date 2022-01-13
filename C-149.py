'''
Created on 2021/09/20

@author: kentoo
'''
X = int(input())

while (1):
    flag = True 
    for  i in range(2,X):
        if X%i==0:
            flag = False
            break
    if flag:
        break 
    X += 1
print(X)
    