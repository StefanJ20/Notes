# This Section Represents Notes On Algorithms done in Python.

# Binary Search Algorithm #

A binary search algorithm utilizes a sorted list of elements, divides the list in half, and works its way in a divided manner until it finds the indexed search result. Access to any element of the array should be constant time. This search algorithm starts with searching the middle index. If the searched element isn't found within the middle index, we find if the element we're searching for is greater than or less the selected element. If it is, we search the right side of the list. If not, we search the left. We continue this process until we reach our goal. We use bisect_left to find the position where x should be inserted.

```python

import bisect

def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search_bisect(arr, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

```

# Merge Sort #

Merge sort is an `(O(log n))` sorting algorithm that takes an existing arrays, divides it into multiple subarrays and conquers by sorting the divided values into a new array. The steps are as follow: Divide; you divide the array into subarrays with individual elements. Conquer; you check to see if the elements are properly sorted within their subarrays, if not you sort them into the new merged array. Merge; all elements are pushed into a new array. 


```python

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0 
    k = left

    while i < n1 and j < n2: 
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


```

# Quick Sort #

A quick sort alogirthm starts by initializing a pointer, usually at the beginning or end of the list, and moving through each indice around the pointer to check if the value is greater than or less than the pointer, and then swapping it accordingly. The function chooses a pivot, partitions all the numbers less than it to the lft, and all the numbers greater than it to the right, and recursively completes this process until the list is sorted.

```python

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)


```

# BFS (Breadth-First Search) #

This is a search algorithm with runtime complexity O(V + E) that searches every possible node adjecent to the current discovered nodes before completing all teraversal operations. This search algorithm isn't incredibly efficient, requiring a large number of traversals before reaching a goal. Possible applications of BFS could be web crawlers, Network Security, Social connections in social media apps, etc.

```python

from collections import defaultdict

class Graph:
    __init__(self):
        self.graph = defaultdict(list) # init for self with a defaultdict library list initialized

    def addEdge(self, u, v):
        self.graph[u].append(v) # append a node to another node.

    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1) # set all nodes to false

        queue = [] # empty queue init

        queue.append[s] # append root node from search
        visited[s] = True # Change its state

        while queue: # while a queue exists

            s = queue.pop[0] # pop the first item in the queue
            print(s, end=" ") # neat print

            for i in self.graph[s]: # loops through all objects currently in the graph's queue, changing the truth value accordingly.
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


```
# Depth-First Search #

Depth First Search algorithm is a search algorithm, similar to Breadth first search with a runtime complexity of O(V + E). The difference is, on average, depth first search goes through less vertices and edges on average, so it will have a shorter runtime despite the same complexity. This algorithm works by choosing a starting node and a goal node, traversing through the least amount of nodes by searching with depth first. 

```python

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, u):
        self.graph[v].append(u)

    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end=' ')

        for i in self.graph[v]:
            if i not in visited:
                self.DFSUtil(i, visited)

    def DFS(self, v):

        visited = set()
        self.DFSUtil(v, visited)
```

# Two Sums #

```python

def TwoSums(nums, target):
    map = {}
    for i, num in enumerate(nums):
        complement = num - target
        if complement in map:
            return [map[complement], i]
        map[num] = i

nums = [2, 7, 11, 15]
target = 26
print(TwoSums(nums, target))  # Output: [0, 1]

```
# Longest Palindrome in substring #

```python

def longestPalindrome(self, s):
    if not s:
        return ""
    start = 0
    end = 0
    for i in range(len(s)):
        l1, r1 = self.expand(s, i, i)
        if r1 - l1 > end - start:
            start, end = l1, r1
        l2, r2 = self.expand(s, i, i + 1)
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end + 1]
def expand(self, s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1


```
# Contains duplicate #

```python

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False

```

# Majority Element

```python

    def majorityElement(self, nums):
        candidate = None
        count = 0

        for i in nums:
            if count == 0:
                candidate = i
            
            if i == candidate:
                count +=1
            else:
                count -=1
        return candidate

```

# Is Anagram #

```python

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        mp1 = {}
        mp2 = {}

        for i in s:
            mp1[i] = mp1.get(i, 0) + 1

        for j in t:
            mp2[j] = mp2.get(j, 0) + 1

        return mp1 == mp2

```

# Length of the longest substring without repeating characters #



```python

    def lengthOfLongestSubstring(self, s):
        l = r = bestLen = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                bestLen = max(bestLen, r - l + 1)
                r += 1
            else:
                seen.discard(s[l])
                l += 1
        return bestLen

```
# Longest possible palindrome in substring

The logic here is O(n), iterating once through every element rather than finding a palindrome directly. Intialize set, length, and loop through the string for unique characters. In the character exists, remove it, increment len by 2, else we just add the character to the set. If anything remains in the set (odd palindrome) we increment it by 1 at the end. Return the length.

```python

    def longestPalindrome(self, s):
        odd = set()
        len = 0

        for ch in s:
            if ch in odd:
                odd.remove(ch)
                len += 2
            else: 
                odd.add(ch)
        
        if odd:
            len += 1

        return len

```

# Rotting Oranges #

Also utilizing BFS algorithm, this time queueing rotted oranges and initializing ripe ones. we iterate with  `for _ in range(len(q))` incrementing minutes after every for loop.

```python

from collections import deque

class Solution(object):
    def orangesRotting(self, grid):

        rows = len(grid)
        columns = len(grid[0])

        q = deque()
        visited = set()
        minutes = fresh = 0 

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    visited.add((r, c))
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited and grid[nr][nc] == 1):
                
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                    
                        q.append((nr, nc))
                        visited.add((nr, nc))

            minutes += 1
        if fresh == 0:
            return minutes
        else:
            return -1
        

```

# Number of Islands #

Logic follows BFS search, starting at a specific row and column and moves through finding neighboring islands. 

```python

from collections import deque

def numIslands(grid):
    row = len(grid)
    col = len(grid[0])
    islands = 0
    visited = set()

    def BFS(StartR, StartC):
        q = deque()
        visited.add((StartR, StartC))
        q.append((StartR, StartC))

        while q:
            r, c = q.popleft()
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    q.append((nr, nc))
            
    for r in range(rows):
        for c in range(col):
            if grid[r][c] == 1 and (r, c) not in visited:
                BFS(r, c)
                islands += 1
    
    return islands


```

# Walls and Gates #

Approach without using a set, just the constant representing a room. Logic follows BFS.

```python
from collections import deque

def wallsAndGates(room):
    if not room or not room[0]:
        return

    q = deque()
    rows, cols = len(room), len(room[0])

    INF = 999999999

    for r in range(rows):
        for c in range(cols):
            if room[r][c] == 0:
                q.append((r, c))
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and room[nr][nc] == INF:
            q.append((nr, nc))
            room[nr][nc] = room[r][c] + 1

```

# Group Anagrams #

3 Things to keep in mind here: Sorting them with the key, appending the key to groups, returning a list of all of groups values.

```python 

from collections import defaultdict

def groupAnagram(self, strs):

    groups = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)

    return list(groups.values())

```

