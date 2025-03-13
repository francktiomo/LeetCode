# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/

import math
import string
import time

class Solution(object):
	def __init__(self):
		self.letters: str = string.ascii_lowercase
		self.TRANSFORMATIONS: dict[str, str] = {
			'a': 'b',
			'b': 'c',
			'c': 'd',
			'd': 'e',
			'e': 'f',
			'f': 'g',
			'g': 'h',
			'h': 'i',
			'i': 'j',
			'j': 'k',
			'k': 'l',
			'l': 'm',
			'm': 'n',
			'n': 'o',
			'o': 'p',
			'p': 'q',
			'q': 'r',
			'r': 's',
			's': 't',
			't': 'u',
			'u': 'v',
			'v': 'w',
			'w': 'x',
			'x': 'y',
			'y': 'z',
			'z': 'ab'
		}
		  
	# def get_next_letter(self, curr_letter: str):
	# 	curr_letter_idx: int = self.letters.index(curr_letter)
	# 	return self.letters[curr_letter_idx + 1]
        
	def lengthAfterTransformations(self, s: str, t: int):
		"""
		:type s: str
		:type t: int
		:rtype: int
		"""
		curr_str: str = s
		count = 0
		for i in range(0, t):
			transformed_str = ''
			for letter in set(curr_str):
				# next_letter = 'ab' if letter == 'z' else self.get_next_letter(letter)
				transformed_str += self.TRANSFORMATIONS[letter]*curr_str.count(letter)
				count += 2 if letter == 'z' else 0
			curr_str = transformed_str
			# print(f'Current string for t={i}: {curr_str}')
					
		return int(count % (math.pow(10, 7) + 7))

# 79033769
solution = Solution()
start = time.time()
response = solution.lengthAfterTransformations('jqktcurgdvlibczdsvnsg', 7517)
print(response)
print(f'Time taken: {time.time() - start}')

# for idx, letter in enumerate('ket'):
# 	print(f'{idx} => {letter}')

# test = {
# 	'a': 'b',
# 	'c': 'd',
# 	'e': 'd'
# }

# for t in test:
# 	print(test[t])
