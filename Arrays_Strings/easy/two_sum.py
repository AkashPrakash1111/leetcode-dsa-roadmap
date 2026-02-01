"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Arrays & Strings

Approach:
- Use a hashmap to store numbers we have seen so far
- For each number, check if (target - current number) exists
- If yes, return the stored index and current index

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

