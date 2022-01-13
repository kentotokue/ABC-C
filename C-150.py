'''
Created on 2021/09/18

@author: kentoo
'''
import itertools
N = int(input())

P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

J = list(itertools.permutations(P))
J.sort()


a = J.index(P)
b = J.index(Q)

print(abs(a-b))
      