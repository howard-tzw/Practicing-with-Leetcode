# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


stack = ['1', 'b', 'c']
print(stack[-1])

# mine


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in bracket_map:
                stack.append(bracket_map[char])
            else:
                if stack and char == stack[-1]:
                    stack.pop()
                else:
                    return False

        return stack == []
