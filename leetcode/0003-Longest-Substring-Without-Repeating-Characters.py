# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastPos = {}
        start = maxLen = 0
        for i, ch in enumerate(s):
            if ch in lastPos and lastPos[ch] >= start:
                start = lastPos[ch] + 1
            lastPos[ch] = i
            maxLen = max(maxLen, i - start + 1)
        return maxLen

# me


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat = {}
        start = 0
        maxLen = 0
        for i, char in enumerate(s):
            if char in repeat and repeat[char] >= start:
                start = repeat[char] + 1
            repeat[char] = i
            maxLen = max(maxLen, i - start + 1)
        return maxLen
