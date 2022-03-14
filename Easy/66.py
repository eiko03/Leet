class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ite = len(digits)-1
        adder = 1
        while adder != 0:
            if ite < 0:
                digits.insert(0,0)
                ite = 0
   
            digits[ite] += adder

            if digits[ite] > 9:
                adder = int(digits[ite] / 10)
                digits[ite] = digits[ite] % 10
            else:
                adder -= 1
            ite -= 1
        return digits
