# https://leetcode.com/problems/find-the-original-typed-string-ii/description/


class Solution(object):
    def possibleStringCount(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        max_len = len(word)
        count = 0
        possible_string = ''

        

