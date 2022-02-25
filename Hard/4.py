# Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        anslist=nums1+nums2
        anslist.sort()
        length=len(anslist)
        if length%2 != 0:
            return anslist[int((length/2)-0.5)]
        else:
            return (anslist[int(length/2)]+anslist[int((length/2)-1)])/2