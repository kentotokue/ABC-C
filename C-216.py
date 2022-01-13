'''
Created on 2021/08/29

@author: kentoo
'''

N = int(input())
'''
i=0
sum = 1
ans = ["A"]
while i<=120:
    i+=1
    if sum*2 <= N:
        sum*=2
        ans.append("B")
    else:
        sum+=1
        ans.append("A")
        
    if sum==N:
        break
print(ans)
'''

ans = []

while N :
    if N%2==0:
        ans.append("B")
        N=N//2
    else:
        ans.append("A")
        N-=1
ans.reverse()

for i in range(len(ans)):
    print(ans[i],end="")