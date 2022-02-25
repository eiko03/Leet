# Permutations

class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		queue = [(nums, [])]
		res = []
		while queue:
			n, perm = queue.pop(0)
			if len(perm) == len(nums):
				res.append(perm)
			else:
				for i in range(len(n)):
					new_n = n[:i] + n[i + 1:]
					queue.append((new_n, perm + [n[i]]))
		return res