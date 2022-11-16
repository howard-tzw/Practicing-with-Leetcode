# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# mine


class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i, char in enumerate(str(x)):
            j = len(str(x)) - 1 - i
            if i is not j and char != str(x)[j]:
                return False

        return True
