# https://leetcode.com/problems/longest-palindromic-substring/
# https://hackmd.io/@CynthiaChuang/LeetCode-0005-Longest-Palindromic-Substring

# 超難，還沒搞懂...
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        s = "$#" + "#".join(s) + "#@"
        radii = [0] * len(s)
        max_right, center = 0, 0

        for idx, char in enumerate(s[1:-1], start=1):
            if idx < max_right:
                radii[idx] = min(
                    radii[center - (idx - center)], max_right - idx)

            while s[idx+(radii[idx]+1)] == s[idx-(radii[idx]+1)]:
                radii[idx] += 1

            if idx + radii[idx] > max_right:
                max_right = idx + radii[idx]
                center = idx

        max_radius = max(radii)
        max_radius_idx = radii.index(max_radius)
        palindrome = s[max_radius_idx -
                       max_radius: max_radius_idx+max_radius+1].replace("#", "")

        return palindrome
