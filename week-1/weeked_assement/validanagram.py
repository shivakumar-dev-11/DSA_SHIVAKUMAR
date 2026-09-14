#LC_242 VALID ANAGRAM
#https://leetcode.com/problems/valid-anagram/description/
#APPROACH : HERE WE USE THE DICTIONARY TO STORE THE FREQUENCY OF
#  THE CHARACTERS IN THE FIRST STRING AND THEN WE CHECK THE SECOND 
# STRING IF THE CHARACTER IS PRESENT IN THE DICTIONARY AND DECREASE THE FREQUENCY OF THAT CHARACTER
#  IF THE FREQUENCY OF THAT CHARACTER IS LESS THAN 0 THEN WE RETURN FALSE
#TIME COMPLEXITY : O(n)
#STATUS : SUCCESS SOLVED IN 20 MINS
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        freq = {}
        for i in s :
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in t :
            if i in freq:
                freq[i] -=1
            else:
                return False
        for i in freq:
            if freq[i] != 0:
                return False

        return True      


            




       
    

       
      

            