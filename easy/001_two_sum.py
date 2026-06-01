# Problem: Two Sum — LeetCode #1
# Difficulty: Easy
# Pattern: Arrays & Hashing
# Link: https://leetcode.com/problems/two-sum/
# Time: O(n) | Space: O(n)
#
# Intuition:
# For each number, check if its complement (target - num) already exists.
# Use a hashmap to store seen numbers for O(1) lookup.
#
# Approach:
# 1. Create a hashmap {value: index}
# 2. For each num, check if (target - num) is in the map
# 3. If yes, return [map[complement], current_index]
# 4. If no, add num to map and continue

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

# Key insight to remember:
# Store what you've SEEN, check for what you NEED.
