# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        k = 0
        while k < len(words):
            currentString = ''.join(words[:k])
            if currentString == s:
                return True
            k += 1
        return False
