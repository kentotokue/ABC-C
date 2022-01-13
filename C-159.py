'''
Created on 2021/09/10

@author: kentoo
'''

L = int(input())

X = L/3
ans = X**3

print(ans)


'''
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            if ((i+j+k)==L):
                area = i*j*k 
            ans = max(area,ans)

print(ans)
'''             