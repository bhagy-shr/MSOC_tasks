# Week 2 - Python Programming

Welcome to Week 2 of the Data Science Track! 

This week focuses on strengthening your Python fundamentals through practical coding tasks. By completing these exercises, you will gain hands-on experience with core Python concepts that are widely used in Data Science, Machine Learning, and AI development.

You will also receive a separate NumPy problem set this week. Unlike traditional programming exercises, the NumPy tasks will introduce you to the way Data Scientists and Machine Learning Engineers write efficient, industry-level code.

---

# Task 1: Find Unique Elements from an Array

**Difficulty:** Easy 

## Problem Statement

Write a Python program that:

1. Takes an array (list) as input from the user.
2. Passes the array to a function.
3. The function should return all unique elements present in the array.
4. Display the unique elements to the user.

### Example

Input:

```python
[1, 2, 3, 2, 4, 1, 5]
```

Output:

```python
[1, 2, 3, 4, 5]
```

## Learning Objectives

* Variables
* Lists
* Loops
* Functions
* Basic Python Syntax

After completing this task, you should be comfortable writing loops and functions in Python, especially if you already have experience with C/C++.

---

# Task 2: Matrix Operations

**Difficulty:** Medium 

## Problem Statement

### Part A: Matrix Transpose

Given a matrix, print its transpose.

Example:

Input:

```text
1 2 3
4 5 6
```

Output:

```text
1 4
2 5
3 6
```

### Part B: Diagonal Sums

For a square matrix, calculate:

* Primary Diagonal Sum
* Secondary Diagonal Sum

Example:

Input:

```text
1 2 3
4 5 6
7 8 9
```

Output:

```text
Primary Diagonal Sum = 15
Secondary Diagonal Sum = 15
```

## Learning Objectives

* Working with 2D Lists (Matrices)
* Nested Loops
* Matrix Traversal
* Index-Based Operations

After completing this task, you will understand how matrices are represented and manipulated in Python.

---

# Task 3: String Tokenization

**Difficulty:** Hard ⭐⭐⭐

## Problem Statement

Tokenization is one of the most fundamental concepts used in Natural Language Processing (NLP) and Large Language Models (LLMs).

Your task is to tokenize a given string into individual words.

Example:

Input:

```python
"I am Tirth Patel"
```

Output:

```python
["I", "am", "Tirth", "Patel"]
```

### Dataset

Use the following code to download the text data:

```python
import requests

url = "https://raw.githubusercontent.com/spyguessgame-boop/own_dataset/refs/heads/main/data.txt"

response = requests.get(url)
response.raise_for_status()

text_data = response.text

text_data = text_data[:1000]
print(text_data)
```

Run the code above to obtain the text and then write a Python program that tokenizes the content into words.

### Bonus Challenge

* Count the total number of tokens.
* Find the most frequent token.
* Remove punctuation before tokenization.

## Learning Objectives

* String Manipulation
* Text Processing
* Lists
* Real-World Data Handling
* Introduction to NLP and LLM Pipelines

Tokenization may appear simple, but it is one of the first and most important steps in how modern LLMs process text.

---

# Submission Guidelines

* Write clean and readable code.
* Add comments wherever necessary.
* Push your solutions to your GitHub repository.
* Ensure that your code runs without errors.

Happy Coding! 
