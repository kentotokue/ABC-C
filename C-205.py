'''
Created on 2021/06/19

@author: kentoo
'''

A,B,C=map(int,input().split())

if C%2!=0:
    if A>B:
        print(">")
    elif A<B:
        print("<")
    else:
        print("=")
else:
    if abs(A)>abs(B):
        print(">")
    elif abs(A)<abs(B):
        print("<")
    else:
        print("=")