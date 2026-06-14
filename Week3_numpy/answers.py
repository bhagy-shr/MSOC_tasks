import numpy as np # type: ignore

"""PROBLEM 1"""
arr=eval(input("List of numbers: "))
arr=np.array(arr)

print(f"Sum = {arr.sum()}\nMean = {arr.mean()}\nMax = {arr.max()}")


"""PROBLEM 2"""
arr=np.array(eval(input("List of numbers: ")))
arr=arr[arr%2==0]
print(arr)


"""PROBLEM 3"""
l=[]
n=int(input("Enter No of rows:"))
for i in range(n):
    l.append(list(map(int,input().split())))

arr=np.array(l)
max_index=max(range(n), key=lambda i : sum(arr[i]))
#key denotes the method by which the i is chosen which is maximising the sum of a row.
print(max_index)


"""PROBLEM 4"""
l=[]
n=int(input("enter no of students:"))
for i in range(n):
    l.append(list(map(int, input().split())))

arr=np.array(l)
ans=[]
for i in range(n):
   if arr[i].mean()>75 :
       ans.append(i)
print(ans)



"""PROBLEM 5"""
n=int(input("Enter number of servers: "))
l=[]
avg=np.zeros(n)
for i in range(n):
    l.append(list(map(int, input().split())))
    avg[i]=sum(l[i])/len(l[i])

#since we cannot add or delete thing synamically in a numpy array, I have used list as input, 
#we can if wish to convert the list in numpy array and do the same operations

total_avg=avg.mean()
ans=np.where(avg>2*total_avg)[0].tolist()
print(ans)


"""PROBLEM 6"""
t=np.array(eval(input("Enter transactions: "))) #we can take such input in problem 5 too.
k=int(input("Enter K:"))

scores = 0.6*t[:,0] + 0.3*t[:,1] + 0.1*t[:,2]

#method 1
idx=np.argsort(scores)[::-1]#sorting indexes using scores and then reversing it for decending order

print("Method 1 Answers")
for i in range(k):
    print(idx[i], ":" , scores[idx[i]])

#method 2
risk=[]
for i in range(t.shape[0]):
    risk.append((scores[i],i))
risk.sort(reverse=True)

print("Method 2 Answers")
for i in range(k):
    print(risk[i][1],":",risk[i][0])

