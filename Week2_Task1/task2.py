import numpy as np # type: ignore

"""PART A"""

l=[]
n=int(input())


for i in range(n):
    l.append(list(map(int,input().split())))

x=np.array(l).T

#print(x.shape)
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        print(x[i][j],end=" ")
    print("")


"""PART B"""

l=[]
n=int(input())

for i in range(n):
    l.append(list(map(int,input().split())))

s1=0 #principal diagonal
s2=0 #secondary diagonal

for i in range(3):
    for j in range(3):
        if(i==j): s1+=l[i][j]
        if(i+j==n-1): s2+=l[i][j]

print(f"Primary Diagonal Sum={s1} \nSecondary Diagonal Sum={s2}")

