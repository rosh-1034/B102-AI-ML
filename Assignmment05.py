# 1. Find the second-largest unique element without using sort() or max()
arr = [10, 20, 5, 20, 15]

largest = None
second = None

for num in arr:
    if largest is None or num > largest:
        second = largest
        largest = num

    elif num != largest and (second is None or num > second):
        second = num

if second is None:
    print("Second largest does not exist")
else:
    print("Second largest:", second)

#         ***********

    # 2. Find all pairs in an array whose sum equals a given target.
arr = [2, 4, 3, 5, 7, 8, 1]
target = 9

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])

#         ***********

#3) Move all zeros to the end
arr = [0, 1, 0, 3, 12]

result = []

for num in arr:
    if num != 0:
        result.append(num)

for num in arr:
    if num == 0:
        result.append(0)


print(result)

#         ***********

# 4) Find the missing number from 1 to N
arr = [1, 2, 4, 5]
n = 5

total = n * (n + 1) // 2
missing = total - sum(arr)

print("Missing number:", missing)

#         ***********


# 5. Find all duplicate elements without nested loops
arr = [1, 2, 3, 2, 4, 5, 1]

seen = set()
duplicate = set()

for num in arr:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)

print(duplicate)

#         ***********

# 6. Find the first non-repeating character
s = "swiss"

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:", ch)
        break

#         ***********

# 7. Check whether two strings are anagrams without sorted()
s1 = "listen"
s2 = "silent"

if len(s1) == len(s2):
    if all(s1.count(ch) == s2.count(ch) for ch in set(s1)):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")

#         ***********

# 8. Merge two sorted arrays without sort()
a = [1, 3, 5]
b = [2, 4, 6]

result = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print(result)

#         ***********

# 9. Rotate an array to the right by K positions
arr = [1, 2, 3, 4, 5]
k = 2

k = k % len(arr)

result = arr[-k:] + arr[:-k]

print(result)

#         ***********

# 10. Find the intersection of two arrays, including duplicates
a = [1, 2, 2, 3, 4]
b = [2, 2, 4, 5]

result = []

for num in a:
    if num in b:
        result.append(num)
        b.remove(num)

print(result)

#         ***********


# 11. Find the maximum sum of a subarray (Kadane's Algorithm)
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = arr[0]
maximum = arr[0]

for num in arr[1:]:
    current = max(num, current + num)
    maximum = max(maximum, current)

print("Maximum sum:", maximum)

#         ***********

# 12. Find the longest substring without repeating characters
s = "abcabcbb"

longest = ""

for i in range(len(s)):
    temp = ""

    for j in range(i, len(s)):
        if s[j] in temp:
            break
        temp += s[j]

    if len(temp) > len(longest):
        longest = temp

print("Longest substring:", longest)
print("Length:", len(longest))

#         ***********

# 13. Find the majority element in an array
arr = [2, 2, 1, 2, 3, 2, 2]

for num in arr:
    if arr.count(num) > len(arr) // 2:
        print("Majority element:", num)
        break

#         ***********


# 14. Find the longest consecutive sequence
arr = [100, 4, 200, 1, 3, 2]

s = set(arr)
longest = 0

for num in s:
    if num - 1 not in s:
        count = 1

        while num + count in s:
            count += 1

        longest = max(longest, count)

print("Longest sequence:", longest)

#         ***********

# 15. Find the product of array elements except self
arr = [1, 2, 3, 4]

result = []

for i in range(len(arr)):
    product = 1

    for j in range(len(arr)):
        if i != j:
            product = product * arr[j]

    result.append(product)

print(result)

#         ***********

# 16. Find the smallest missing positive number
arr = [3, 4, -1, 1]

num = 1

while num in arr:
    num += 1

print("Smallest missing positive:", num)

#         ***********

# 17. Check balanced parentheses using Stack
s = "{[()]}"

stack = []
pairs = {')': '(', '}': '{', ']': '['}

for ch in s:
    if ch in "({[":
        stack.append(ch)

    elif ch in ")}]":
        if not stack or stack.pop() != pairs[ch]:
            print("Not Balanced")
            break
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")

#         ***********


# 18. Implement a Queue using a List
queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

queue.pop(0)

print("After deletion:", queue)

#         ***********

# 19. Implement a Stack using a List

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

stack.pop()

print("After deletion:", stack)

#         ***********

# 20. Binary Search in a sorted array

arr = [10, 20, 30, 40, 50]
target = 30

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Element not found")

#         ***********

# 21. Find the factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#         ***********


# 22. Print Fibonacci series using recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(7):
    print(fib(i), end=" ")

#         ***********

# 23. Find GCD of two numbers

a = 12
b = 18

while b != 0:
    a, b = b, a % b

print("GCD:", a)

#         ***********

# 24. Find LCM of two numbers
a = 12
b = 18

x = a
y = b

while b != 0:
    a, b = b, a % b

gcd = a
lcm = (x * y) // gcd

print("LCM:", lcm)

#         ***********

# 25. Check whether a number is an Armstrong number
num = 153
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** 3
    temp = temp // 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")

#         ***********

# 26. Find the sum of digits of a number

num = 1234
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum:", total)

#         ***********

# 27. Reverse a number without converting it into a string

num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse:", reverse)

#         ***********

# 28. Check whether a number is a palindrome

num = 121
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#         ***********

# 29. Find the power of a number without using **

base = 2
power = 5
result = 1

for i in range(power):
    result = result * base

print("Answer:", result)

#         **********


# 30. Find the frequency of each element in a list

arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

#         ***********


# 31. Find the Fibonacci number using Dynamic Programming
n = 7

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

#         ***********

# 32. Find the number of ways to climb stairs

n = 5

dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

print("Ways:", dp[n])

#         ***********

# 33. Find the maximum element in a matrix
matrix = [
    [1, 5, 3],
    [7, 2, 9],
    [4, 6, 8]
]

largest = matrix[0][0]

for row in matrix:
    for num in row:
        if num > largest:
            largest = num

print("Largest:", largest)

#         ***********

# 34. Transpose a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = []

for i in range(3):
    row = []
    for j in range(2):
        row.append(matrix[j][i])
    result.append(row)

print(result)

#         ***********

# 35. Implement a Graph using an Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

for node in graph:
    print(node, ":", graph[node])

#         ***********


# 36. Perform Breadth First Search (BFS)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

queue = ['A']
visited = []

while queue:
    node = queue.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        queue.extend(graph[node])

#         ***********


# 37. Perform Depth First Search (DFS)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in graph[node]:
            dfs(neighbour)

dfs('A')

#         ***********


# 38. Generate all permutations of a string

from itertools import permutations

s = "ABC"

result = permutations(s)

for p in result:
    print("".join(p))


#         ***********


# 39. Solve the N-Queens problem (4 Queens)
def solve(row, board):
    if row == 4:
        for r in board:
            print(r)
        print()
        return

    for col in range(4):
        safe = True

        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                safe = False
                break

        if safe:
            board[row] = col
            solve(row + 1, board)

board = [-1] * 4
solve(0, board)

#         ***********

# 40. Implement a Binary Search Tree (BST)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = None

for num in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, num)

inorder(root)