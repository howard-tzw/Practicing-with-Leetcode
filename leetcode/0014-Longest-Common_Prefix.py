
# https://leetcode.com/problems/longest-common-prefix/description/
# learn zip, star sign before list, "".join()

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)

# # mine


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i, word in enumerate(strs):
            if i == 0:
                continue

            for j, char in enumerate(res):
                if j > len(word)-1 or char != word[j]:
                    res = res[:j]

        return res


for val in zip('ab', 'aa'):
    print(val)
