# Integer to Roman

class Solution:

    def takeClosest(self ,myNumber, myList):
        closes t =[i for i in  myList if i  <= myNumber]
        return max(closest)

    def intToRoman(self, num: int) -> str:
        so l =""
        hashma p ={
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

        while nu m >0:
            re s =self.takeClosest(num, list(hashmap.keys()))
            if num == res:
                so l+= hashmap[res]
                nu m =0
            elif nu m %res == 0:
                so l+ =(int(num / res )* hashmap[res])
                nu m =0
            else:
                so l+= hashmap[res]
            nu m- =res

        return sol


