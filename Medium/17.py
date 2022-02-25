# Letter Combinations of a Phone Number

import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if (len(digits) == 0):
            return []

        hashmap = dict()
        hashmap["2"] = ["a", "b", "c"]
        hashmap["3"] = ["d", "e", "f"]
        hashmap["4"] = ["g", "h", "i"]
        hashmap["5"] = ["j", "k", "l"]
        hashmap["6"] = ["m", "n", "o"]
        hashmap["7"] = ["p", "q", "r", "s"]
        hashmap["8"] = ["t", "u", "v"]
        hashmap["9"] = ["w", "x", "y", "z"]

        if (len(digits) == 1):
            return hashmap[digits]

        res = list(hashmap[digits[0]])

        for digit in list(digits[1:]):
            res = ["".join(tupl) for tupl in itertools.product(res, hashmap[digit])]

        return (res)