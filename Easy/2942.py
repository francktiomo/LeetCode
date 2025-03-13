# https://leetcode.com/problems/find-words-containing-character/

def findWordsContaining(words, x):
    """
    :type words: List[str]
    :type x: str
    :rtype: List[int]
    """
    result = []
    for idx, word in enumerate(words):
        if x in word:
            result.append(idx)
    
    return result

print(findWordsContaining(["apple", "banana", "cherry", "date"], "a"))