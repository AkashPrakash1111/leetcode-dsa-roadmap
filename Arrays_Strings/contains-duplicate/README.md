````md

\# 🚀 Contains Duplicate — HashSet Pattern Mastery



---



\## 📌 Problem Overview



Given an integer array `nums`, return:



\- `True` → if any value appears \*\*at least twice\*\*

\- `False` → if all elements are unique  



🔗 LeetCode Problem: https://leetcode.com/problems/contains-duplicate/



---



\## 🧠 Why This Problem Matters



This is a foundational \*\*hashing problem\*\* that introduces:



\- Efficient duplicate detection  

\- HashSet for constant-time lookups  

\- Time vs Space tradeoffs  



Understanding this pattern helps in solving many frequency-based problems.



---



\## 🐢 Brute Force Approach



\### 💡 Idea



Compare every element with every other element using nested loops.



---



\### 🧪 Brute Force Code



```python

class Solution:

&nbsp;   def containsDuplicate(self, nums):

&nbsp;       n = len(nums)



&nbsp;       for i in range(n):

&nbsp;           for j in range(i + 1, n):

&nbsp;               if nums\[i] == nums\[j]:

&nbsp;                   return True



&nbsp;       return False

````



---



\### ⏱ Complexity (Brute Force)



\* \*\*Time:\*\* O(n²) ❌

\* \*\*Space:\*\* O(1) ✅



Nested loops cause quadratic time complexity.



---



\## ⚖️ Better Approach — Sorting



\### 💡 Core Insight



If duplicates exist, after sorting they will be \*\*adjacent\*\*.



---



\### 🧪 Sorting Code



```python

class Solution:

&nbsp;   def containsDuplicate(self, nums):

&nbsp;       nums.sort()



&nbsp;       for i in range(len(nums) - 1):

&nbsp;           if nums\[i] == nums\[i + 1]:

&nbsp;               return True



&nbsp;       return False

```



---



\### ⏱ Complexity (Sorting)



\* \*\*Time:\*\* O(n log n)

\* \*\*Space:\*\* Depends on sorting implementation



Improves time complexity but still not optimal.



---



\## 🚀 Optimal Approach — HashSet



\### 🔑 Core Idea



A \*\*set cannot contain duplicates\*\*.



\* Traverse the array

\* If element already exists in set → duplicate found

\* Otherwise, add it



---



\### ✅ Optimized Code



```python

class Solution:

&nbsp;   def containsDuplicate(self, nums):

&nbsp;       seen = set()



&nbsp;       for num in nums:

&nbsp;           if num in seen:

&nbsp;               return True

&nbsp;           seen.add(num)



&nbsp;       return False

```



---



\### ⏱ Complexity (Optimal)



\* \*\*Time:\*\* O(n) ✅

\* \*\*Space:\*\* O(n) ✅



Single pass with constant-time lookups.



---



\## 🔥 Even Cleaner Version



```python

class Solution:

&nbsp;   def containsDuplicate(self, nums):

&nbsp;       return len(nums) != len(set(nums))

```



\### 💡 Why This Works



If duplicates exist → set size becomes smaller than original list.



---



\## ⚖️ Tradeoff Summary



| Approach    | Time       | Space   |

| ----------- | ---------- | ------- |

| Brute Force | O(n²)      | O(1)    |

| Sorting     | O(n log n) | Depends |

| HashSet     | O(n)       | O(n)    |



---



\## 🔁 Pattern Recognition



If a problem mentions:



\* Checking duplicates

\* Frequency counting

\* Unique elements



👉 Think: \*\*HashSet / HashMap\*\*



---



\## 🧩 Final Takeaway



\* Brute force is simple but inefficient

\* Sorting improves time but changes order

\* HashSet gives optimal linear-time performance

\* Classic example of \*\*Time vs Space tradeoff\*\*



Time Complexity: O(n)

Space Complexity: O(n)



---



\## ✍️ My Handwritten Notes



!\[Handwritten Notes - Contains Duplicate](./notes/contains\_duplicate\_notes.png)



```

```



