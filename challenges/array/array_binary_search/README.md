# Binary Search
From wikipedia... "In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array."

## Challenge
Write a function called binary_search() that takes in 2 arguments: a sorted array and the search key. The function should use the binary search algorithm and return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Solution
![Solution](/assets/array_binary_search.jpeg)

## Big-O
**Time:** O(log n)
**Space:** O(1)
