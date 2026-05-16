````md

\# 🚀 Find Pivot Index — Prefix Sum Pattern Mastery



\---



\## 📌 Problem Overview



Given an integer array `nums`, find the \*\*pivot index\*\*.



A pivot index is where:



\- Sum of all elements to the \*\*left\*\*

&#x20; =

\- Sum of all elements to the \*\*right\*\*



Return the \*\*leftmost pivot index\*\*.



If no pivot index exists → return `-1`.



🔗 LeetCode Problem: https://leetcode.com/problems/find-pivot-index/



\---



\## 🧠 Why This Problem Matters



This problem introduces one of the most important DSA concepts:



\# ➜ Prefix Sum / Running Sum



Instead of recalculating sums repeatedly, we maintain information dynamically while traversing the array.



This pattern appears in many advanced problems involving:



\- Range queries

\- Subarrays

\- Running calculations

\- Balance conditions

\- Space optimization



\---



\## 🧪 Example



```python

nums = \[1,7,3,6,5,6]

````



At index `3`:



```text

Left Sum  = 1 + 7 + 3 = 11

Right Sum = 5 + 6 = 11

```



✅ Pivot Index = `3`



\---



\# 🔴 Brute Force Approach



\## 💡 Core Idea



For every index:



\* Calculate left sum

\* Calculate right sum

\* Compare both



\---



\## 🧪 Brute Force Code



```python

class Solution:

&#x20;   def pivotIndex(self, nums):

&#x20;       n = len(nums)



&#x20;       for i in range(n):



&#x20;           left\_sum = sum(nums\[:i])

&#x20;           right\_sum = sum(nums\[i + 1:])



&#x20;           if left\_sum == right\_sum:

&#x20;               return i



&#x20;       return -1

```



\---



\## ⏱ Complexity (Brute Force)



\### Time Complexity



For every index:



\* Left sum takes O(n)

\* Right sum takes O(n)



Overall:



```text

O(n²)

```



\---



\### Space Complexity



```text

O(1)

```



(ignoring slicing temporary space in interview-style analysis)



⚠️ Inefficient because sums are recalculated repeatedly.



\---



\# 🚀 Optimal Approach — Prefix Sum



\## 🔑 Important Observation



Instead of calculating left and right sums again and again:



\* Compute total sum once

\* Maintain a running left sum while traversing



Then derive:



```text

right\_sum = total\_sum - left\_sum - nums\[i]

```



\---



\# 🧠 Core Logic



At index `i`:



```text

left\_sum  = sum of elements before i



right\_sum = total\_sum - left\_sum - nums\[i]

```



If:



```text

left\_sum == right\_sum

```



then `i` is the pivot index.



\---



\# ✅ Optimal Code



```python

class Solution:

&#x20;   def pivotIndex(self, nums):



&#x20;       total\_sum = sum(nums)

&#x20;       left\_sum = 0



&#x20;       for i in range(len(nums)):



&#x20;           right\_sum = total\_sum - left\_sum - nums\[i]



&#x20;           if left\_sum == right\_sum:

&#x20;               return i



&#x20;           left\_sum += nums\[i]



&#x20;       return -1

```



\---



\# ⏱ Complexity (Optimal)



\### Time Complexity



```text

O(n)

```



Because:



\* One pass for total sum

\* One traversal through the array



\---



\### Space Complexity



```text

O(1)

```



No extra data structures used.



✔ Efficient

✔ Clean logic

✔ Interview-optimized solution



\---



\# 🔥 Most Important Concept



This problem teaches:



\# ➜ Prefix Sum Technique



Instead of recomputing:



```text

sum(left side)

```



again and again,



we progressively maintain it while traversing.



This dramatically improves efficiency.



\---



\# 🔁 Pattern Recognition



Whenever a problem mentions:



```text

left side vs right side

```



OR



```text

sum before / sum after

```



Think:



\# ➜ Prefix Sum / Running Sum



\---



\# 🧩 Problems Using This Pattern



This concept appears in many important problems:



\* Find Pivot Index

\* Running Sum

\* Subarray Sum

\* Product Except Self

\* Range Sum Query

\* Equilibrium Index



Very important DSA pattern.



\---



\# ⚡ Key Insight



The most important formula:



```text

right\_sum = total\_sum - left\_sum - nums\[i]

```



\### 💡 Why subtract `nums\[i]`?



Because:



```text

total\_sum

```



contains:



\* Left side

\* Current element

\* Right side



So we remove:



\* Left side

\* Current element



to isolate the right side.



\---



\# 🧾 Dry Run



```python

nums = \[1,7,3,6,5,6]



total\_sum = 28

left\_sum = 0

```



\---



\## i = 0



```text

right\_sum = 28 - 0 - 1 = 27

```



```text

0 != 27

```



Update:



```text

left\_sum = 1

```



\---



\## i = 1



```text

right\_sum = 28 - 1 - 7 = 20

```



```text

1 != 20

```



Update:



```text

left\_sum = 8

```



\---



\## i = 2



```text

right\_sum = 28 - 8 - 3 = 17

```



```text

8 != 17

```



Update:



```text

left\_sum = 11

```



\---



\## i = 3



```text

right\_sum = 28 - 11 - 6 = 11

```



```text

11 == 11

```



✅ Return:



```text

3

```



\---



\# 🎯 Interview Understanding



If asked:



> “Why is this O(n)?”



You can explain:



```text

We avoid recalculating left and right sums repeatedly.

Instead, we dynamically maintain left\_sum and derive right\_sum using total\_sum.

```



This reduces repeated work and achieves linear time complexity.



\---



\# 🧠 Core Concepts Used



\* Prefix Sum

\* Running Sum

\* Array Traversal

\* Mathematical Observation

\* Space Optimization



\---



\# 🧩 Final Takeaway



\* Brute force repeatedly recalculates sums

\* Prefix Sum avoids redundant computation

\* Running sums help optimize traversal problems

\* Mathematical observation reduces O(n²) → O(n)



Time Complexity: O(n)

Space Complexity: O(1)



\---



\## ✍️ My Handwritten Notes



!\[Handwritten Notes - Find Pivot Index](./notes/find\_pivot\_index\_notes.png)



```

```



