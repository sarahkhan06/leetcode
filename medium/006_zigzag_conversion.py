# Problem: ZigZag Conversion — LeetCode #6
# Difficulty: Medium
# Pattern: String Manipulation
# Link: https://leetcode.com/problems/zigzag-conversion/
# Time: O(n) | Space: O(n)
#
# Intuition:
# The key insight is that characters are arranged in a repeating zigzag pattern.
# Instead of simulating the zigzag movement, we can group characters by which row they belong to.
# Each character goes to a specific row based on its index and the zigzag direction.
#
# Approach:
# 1. Create an array of strings to represent each row
# 2. Iterate through the string, placing each character in the appropriate row
# 3. Track current row and direction (going down or up)
# 4. When reaching the top or bottom row, reverse direction
# 5. Concatenate all rows to get the result

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row = 0
        going_down = False

        for char in s:
            rows[cur_row] += char

            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down

            cur_row += 1 if going_down else -1

        return "".join(rows)

# Key insight to remember:
# Use direction toggling at boundaries to simulate zigzag without complex math
