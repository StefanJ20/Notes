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
