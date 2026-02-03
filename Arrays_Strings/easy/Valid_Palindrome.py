✅ Valid Palindrome — Brute Force vs Optimized

This problem demonstrates the importance of moving from a brute force approach
to an optimal two-pointer solution, while understanding time and space trade-offs.

🐢 Brute Force Approach

Idea
- Filter only alphanumeric characters
- Convert to lowercase
- Reverse the string and compare

class Solution:
    def isPalindrome(self, s):
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        return cleaned == cleaned[::-1]

❌ Why This Is Not Optimal

The issue is extra work + extra memory.

cleaned += ch

This operation:
- Creates a new string
- Copies all previous characters
- Adds the new character

➡️ Leads to repeated copying (strings are immutable in Python)

cleaned[::-1]

This operation:
- Creates a new reversed string
- Takes O(n) time
- Uses O(n) extra space

⏱ Brute Force Complexity

Time Complexity: O(n²)
Space Complexity: O(n)

🚀 Optimized Approach (Two Pointers)

Idea
- Use two pointers (left, right)
- Skip non-alphanumeric characters
- Compare characters directly
- No extra memory

class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

⏱ Optimized Complexity

Time Complexity: O(n)
- Each character is visited once
- No nested loops
- No string copying

Space Complexity: O(1)
- Only two variables (left, right)
- No extra strings or arrays

🔑 Key Takeaway

- Brute force helps understand the problem
- Two pointers give the best solution
- Avoid unnecessary string creation
- This pattern appears in many string and array problems
