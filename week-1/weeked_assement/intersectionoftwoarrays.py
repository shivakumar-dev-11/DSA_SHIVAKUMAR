#intersectionoftwoarrays
#https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#approach : here  used the 2 pointers if array of i equal to the array of j
#  then append the value to the result and array of j becomes none and we break 
# the loop and the i value increases
#time : O(n²)
#status : success solved in 15 mins

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]

        for i in range (0, len(nums1)):
            for j in range (0 , len(nums2)):
                if nums1[i]== nums2[j]:
                    result.append(nums1[i])
                    nums2[j] = None
                    break
        return result
