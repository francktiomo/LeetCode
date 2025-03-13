from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        numOfPairs = 0
        N = len(words)
        for i in range(N):
            for j in range(i+1, N):
                if words[i] == words[j][::-1]:
                    numOfPairs += 1

        return numOfPairs

if __name__ == '__main__':
    solution = Solution()
    assert solution.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]) == 2
    assert solution.maximumNumberOfStringPairs(["ab","ba","cc"]) == 1
    assert solution.maximumNumberOfStringPairs(["aa","ab"]) == 0
