# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/843308701/
import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data = nums1 + nums2
        data = sorted(data)
        if len(data) % 2 != 0:
            return data[math.ceil(len(data)/2) - 1]
        else:
            return (data[int(len(data) / 2 - 1)] + data[int(len(data) / 2)]) / 2

# mine


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged = sorted(merged)

        if len(merged) % 2:
            return merged[len(merged)//2]
        else:
            return (merged[len(merged)//2] + merged[(len(merged)//2)-1]) / 2
