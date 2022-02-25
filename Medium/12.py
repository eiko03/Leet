# Integer to Roman

class Solution:

    def takeClosest(self ,myNumber, myList):
        closest =[i for i in  myList if i  <= myNumber]
        return max(closest)

    def intToRoman(self, num: int) -> str:
        sol =""
        hashmap ={
            1: "I",
            4 :"IV",
            5: "V",
            9 :"IX",
            10: "X",
            40 :"XL",
            50: "L",
            90 :"XC",
            100: "C",
            400 :"CD",
            500: "D",
            900 :"CM",
            1000: "M"
        }

        while num >0:
            res =self.takeClosest(num, list(hashmap.keys()))
            if num == res:
                sol+= hashmap[res]
                num =0
            elif num %res == 0:
                sol += (int(num / res )* hashmap[res])
                num =0
            else:
                sol+= hashmap[res]
            num -= res

        return sol


