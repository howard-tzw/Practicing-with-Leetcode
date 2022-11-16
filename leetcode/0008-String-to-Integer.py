# https://leetcode.com/problems/string-to-integer-atoi/description/

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        numString = re.findall("^[\+\-]?\d+", s.strip())
        if len(numString) == 0:
            return 0
        if int(numString[0]) > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif int(numString[0]) < pow(-2, 31):
            return pow(-2, 31)
        else:
            return int(numString[0])


# mine
# ref: https://hackmd.io/@CynthiaChuang/LeetCode-0008-String-to-Integer-atoi


class Solution:
    def myAtoi(self, s: str) -> int:
        int_max = pow(2, 31)-1
        int_min = pow(-2, 31)

        res_str = re.match('(^[\+\-]?\d+)', s.strip())

        if not res_str:
            return 0

        res = int(res_str.group(0))
        res = min(int_max, max(int_min, res))
        return res
