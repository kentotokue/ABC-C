'''
Created on 2021/06/28

@author: kentoo
'''
N,K=map(int,input().split())

def G1(x):
    
    result=''.join(sorted(str(x))[::-1])
        
    return int(result)
def G2(x):
    
    result=''.join(sorted(str(x)))
    return int(result)

def F (x):
    return (G1(x)-G2(x))

for _ in range(K):
    N=F(N)
    
print(N)

    


        