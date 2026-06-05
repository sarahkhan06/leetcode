# Problem: Median of Two Sorted Arrays — LeetCode #4
# Difficulty: Hard
# Pattern: Binary Search
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Time: O(log(min(m,n))) | Space: O(1)
#
# Intuition:
# Use binary search on the smaller array to find the correct partition point.
# The median is determined by partitioning the combined array such that
# left half ≤ right half.
#
# Approach:
# 1. Binary search on the smaller array to find partition index i
# 2. Calculate corresponding partition j in the second array
# 3. Check if the partition is valid (left elements ≤ right elements)
# 4. Adjust search space based on validity
# 5. Return median based on total length (even or odd)

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, m

        while l <= r:
            i = (l + r) // 2          # partition in nums1
            j = half - i             # partition in nums2

            Aleft = nums1[i - 1] if i > 0 else float("-inf")
            Aright = nums1[i] if i < m else float("inf")

            Bleft = nums2[j - 1] if j > 0 else float("-inf")
            Bright = nums2[j] if j < n else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

# Key insight to remember:
# Binary search the partition point, not the values. The median is determined
# by balancing the left and right halves, not by finding the middle value.
