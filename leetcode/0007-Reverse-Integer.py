# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31 - 1:
            return 0
        elif x < 0:
            if int("-" + str(x).replace("-", "")[::-1]) < -2**31 or int("-" + str(x).replace("-", "")[::-1]) > 2**31 - 1:
                return 0
            else:
                return int("-" + str(x).replace("-", "")[::-1])
        else:
            if int(str(x)[::-1]) < -2**31 or int(str(x)[::-1]) > 2**31 - 1:
                return 0
            else:
                return int(str(x)[::-1])


class Solution:
    def reverse(self, x: int) -> int:
        if self.isOutOfRange(x):
            return 0
        if x < 0:
            reverse = int("-" + str(x).replace('-', '')[::-1])
            if self.isOutOfRange(reverse):
                return 0
            else:
                return reverse

        else:
            reverse = int(str(x).replace('-', '')[::-1])
            if self.isOutOfRange(reverse):
                return 0
            else:
                return reverse

    def isOutOfRange(self, x):
        if x > 2**31-1 or x < -2**31:
            return True
        else:
            return False
