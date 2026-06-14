MSOC NumPy Problem Set
Welcome to the NumPy Problem Set!

This problem set is designed to help you practice the fundamental concepts of NumPy, one of the most important libraries in Python for numerical computing and data analysis.

Problem 1: Array Statistics
Given a NumPy array, find:

Sum of all elements
Mean of all elements
Maximum element
Example
arr = np.array([1, 2, 3, 4, 5])
Expected Output
Sum = 15
Mean = 3
Max = 5


Problem 2: Even Number Filter
Given a NumPy array, return only the even numbers.

Example
arr = np.array([1, 2, 3, 4, 5, 6])
Expected Output
[2, 4, 6]



Problem 3: Row With Maximum Sum
Given a 2D NumPy array, find the index of the row having the largest sum.

Example
arr = np.array([
    [1, 2, 3],
    [5, 5, 5],
    [2, 2, 2]
])
Expected Output
1
Explanation
Row sums = [6, 15, 6]



Problem 4: Student Performance Analysis
Each row represents a student and each column represents marks in a subject.

Return the indices of students whose average marks are greater than 75.

Example
marks = np.array([
    [80, 90, 70],
    [50, 60, 70],
    [90, 95, 85]
])
Expected Output
[0, 2]
Explanation
Student 0 Average = 80
Student 1 Average = 60
Student 2 Average = 90



Problem 5 Network Traffic Anomaly Detection (Very Hard Version)
A server records requests per minute.
You are given traffic data for many servers.
Return the indices of servers whose traffic is more than 2× the overall average traffic.

traffic = np.array([
 [100,120,110],
 [90,95,100],
 [500,550,600]
])
[2]



Problem 6 Fraud Detection Feature Generator (Very Hard Version)
You are working for a fintech company. Every row represents a customer transaction.
Columns:

[Amount, TimeSpent, FailedAttempts]

Risk Score:
0.6 × normalized(Amount)
+
0.3 × normalized(TimeSpent)
+
0.1 × normalized(FailedAttempts)
Return top K most risky users.
Input :

transactions =
[
[1000,50,0],
[5000,20,2],
[3000,80,5]
]

k = 2
Submission Guidelines
Use NumPy wherever possible.
Avoid using explicit Python loops unless necessary.
Write clean and readable code.
Add comments where appropriate.
Test your solution with different inputs before submission.
Happy Coding! 🎉