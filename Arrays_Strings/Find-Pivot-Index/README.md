# 🎯 Find Pivot Index
> **Pattern:** Prefix Sum · **Difficulty:** Easy · **Topic:** Arrays

![pivot-demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHVtNXVpNXBld3BrMXZrMHprcGo3MzllNnVhYXlzZm1vbzh3NGZsZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oKIPnAiaMCws8nOsE/giphy.gif)

---

## 📌 Problem

> Find the **leftmost pivot index** where `left_sum == right_sum`. Return `-1` if none exists.

🔗 [LeetCode #724](https://leetcode.com/problems/find-pivot-index/)

---

## 🔑 Key Formula

```
right_sum = total_sum - left_sum - nums[i]
```

> This avoids recomputing sums every iteration — the entire trick.

---

## ⚡ Optimal Solution — O(n)

```python
class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
```

---

## 🧪 Dry Run

```
nums = [1, 7, 3, 6, 5, 6]   →   total_sum = 28
```

| i | left_sum | nums[i] | right_sum | Match? |
|---|----------|---------|-----------|--------|
| 0 | 0        | 1       | 27        | ❌     |
| 1 | 1        | 7       | 20        | ❌     |
| 2 | 8        | 3       | 17        | ❌     |
| **3** | **11** | **6** | **11**  | ✅ → return `3` |

---

## 📊 Complexity

| Approach    | Time   | Space |
|-------------|--------|-------|
| Brute Force | O(n²)  | O(1)  |
| Prefix Sum  | **O(n)** | **O(1)** |

---

## 🧠 Pattern Recognition

Spot this pattern when a problem says:

```
"sum of left side"  vs  "sum of right side"
"balance point"
"before index i"    vs  "after index i"
```

→ Think **Prefix Sum / Running Sum** immediately.

---

## 🔁 Related Problems

| Problem | Pattern |
|---------|---------|
| Running Sum of 1D Array | Prefix Sum |
| Subarray Sum Equals K | Prefix Sum + HashMap |
| Product of Array Except Self | Prefix Product |
| Range Sum Query | Prefix Sum |

---
## MY NOTES 



<img width="1280" height="812" alt="672fb940-e06c-476f-b0f3-de4b84584c14" src="https://github.com/user-attachments/assets/fd28f745-c500-4368-ac54-7237c7608334" />


---
> 💡 **Interview tip:** When asked *why O(n)?* — "We avoid recomputing by dynamically maintaining `left_sum` and deriving `right_sum` mathematically from `total_sum`."
