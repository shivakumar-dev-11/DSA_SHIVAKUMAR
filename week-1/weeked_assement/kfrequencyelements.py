#LC_347  K FREQUENCY ELEMENTS
#https://leetcode.com/problems/top-k-frequent-elements/description/
#APPROACH : HERE WE USE THE FREQUENCT TO CALCULATE THE FREQUENCY OF NUMBERS AND 
#WE SORT THEM IN ASSECNDING ORDER AND WE REVERSE THE FREQUENCY AND RETURN THE K FREQUENCY THE USER NEEDED 
#TIME COMPLEXITY : O(n LOG n)
#STATUS : SUCCESS SOLVED IN 25 MINS
class Solution(object):

    def topKFrequent(self, nums, k):

        freq = {}

       
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_num = sorted(freq, key = freq.get, reverse = True )

        return sorted_num [:k]