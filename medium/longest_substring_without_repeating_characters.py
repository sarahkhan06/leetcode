# Problem: Longest Substring Without Repeating Characters — LeetCode #3
# Difficulty: Medium
# Pattern: Sliding Window
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time: O(n) | Space: O(n)
#
# Intuition:
# Keep a window [left, right] with no duplicates.
# Expand right each step. If s[right] is already in the window,
# shrink from the left until it's gone.
#
# Approach:
# 1. Use a set to track characters in the current window
# 2. Move right pointer forward each iteration
# 3. While duplicate found, remove s[left] from set and move left forward
# 4. Update max length after window is valid

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        result = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            result = max(result, right - left + 1)

        return result

# Key insight to remember:
# When you hit a duplicate, shrink LEFT until the duplicate is gone.
# Window size = right - left + 1
