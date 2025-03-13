# https://leetcode.com/problems/reverse-words-in-a-string/submissions/1572654456/?envType=problem-list-v2&envId=string

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)
