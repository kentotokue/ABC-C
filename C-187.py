'''
Created on 2021/06/29

@author: kentoo
'''
N=int(input())

S=set(input() for i in range(N))

for s in S:
    if "!"+s in S:
        print(s)
        exit()
print("satisfiable")