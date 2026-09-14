# LC_ 283 move zeroes to the end
#https://leetcode.com/problems/move-zeroes/description/
#APPROACH : WE CHECK THE ARRAY ELEMENT IF THE ELEMENT IS NOT EQUAL TO ZERO WE  SWAP THE VALUES 
# OF I AND J FOR THAT WE DECLARE J AS 0 AND WE INCREASE J VALUE AFTER EVERY ITERATION OF I AND 
# WE GO THROUGH A LOOP WHERE THE J SHOULD BE LESS THAN ARRAY LENGTH AND THE REMAINING ELEMENTS
#  SHOULD BE DECLARE AS 0
#TIME COMPLEXITY : O(n)
#STATUS : SUCCESS SOLVED IN 15 MINS
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0 
        for i in range (0 , len(nums)):
            if nums[i] != 0:
                nums[j]=nums[i]
                j+=1
        while j < len(nums):
            nums[j]=0
            j+=1