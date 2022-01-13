'''
Created on 2021/12/03

@author: kentoo
'''
N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

Mi1 = max(1-A,1-B)
Ma1 = min(N-A,N-B)
Mi2 = max(1-A,B-N)
Ma2 = min(N-A,B-1)

H = Q - P + 1
W = S - R + 1

for i in range(P-1,Q):
    for j in range(R-1,S):
        KA = (i+1)-A 
        KB1 = (j+1)-B
        KB2 = B-(j+1)
        #print(KA,KB1,KB2)

        if (KA == KB1) and (KA >= Mi1 and Ma1 >= KA):
            print("#",end = "")
        elif (KA == KB2) and (KA >= Mi2 and Ma2 >= KA):
            print("#",end = "")
        else:
            print(".",end = "")
    print("")
