# 🚀 Move Zeroes — Two Pointer Mastery

---

## 📌 Problem Overview

Given an integer array `nums`, move all `0`s to the **end** of the array while:

- preserving the **relative order** of non-zero elements  
- modifying the array **in-place**

No extra array should be used in the optimized solution.

---

## 🐢 Brute Force Approach

### 💡 Idea

1. Create a temporary array  
2. Copy all non-zero elements  
3. Count the number of zeros  
4. Append zeros at the end  
5. Copy everything back to the original array  

---

### 🧪 Brute Force Code

```python
class Solution:
    def moveZeroes(self, nums):
        temp = []
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                temp.append(num)

        temp.extend([0] * zero_count)

        for i in range(len(nums)):
            nums[i] = temp[i]

---

### ⏱ Complexity (Brute Force)

- **Time:** O(n)  
- **Space:** O(n)  

---

## 🚀 Optimized Approach — Two Pointers

### 🔑 Core Insight

- Maintain a pointer that tracks where the next non-zero element should be placed  
- Traverse the array once  
- Swap only when necessary  

---

### ✅ Optimized Code (Best Solution)

```python
class Solution:
    def moveZeroes(self, nums):
        last_non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
```

---

## 🔍 Pointer Breakdown

| Pointer         | Meaning                                    |
|-----------------|--------------------------------------------|
| `i`             | Fast pointer scanning the array            |
| `last_non_zero` | Position where the next non-zero should go |

---

## 🧾 Dry Run Example

**Input**

```
[0, 1, 0, 3, 12]
```

| i | nums[i] | Action | Array           | last_non_zero |
|---|---------|--------|----------------|---------------|
| 0 | 0       | skip   | [0,1,0,3,12]   | 0             |
| 1 | 1       | swap   | [1,0,0,3,12]   | 1             |
| 2 | 0       | skip   | [1,0,0,3,12]   | 1             |
| 3 | 3       | swap   | [1,3,0,0,12]   | 2             |
| 4 | 12      | swap   | [1,3,12,0,0]   | 3             |

---

## 🧩 Final Takeaway

- Brute force is easy but space-inefficient  
- Two pointers give a clean, optimal solution  
- Time Complexity: O(n)  
- Space Complexity: O(1)  

## MY NOTES

![WhatsApp Image 2026-02-10 at 7 22 39 PM](https://github.com/user-attachments/assets/faf3689c-72e3-4037-9e82-a317ab44c294)

