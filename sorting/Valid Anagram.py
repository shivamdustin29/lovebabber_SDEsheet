class Solution(object):
    def isAnagram(self, s, t):
        count1=Counter(s)
    	count2=Counter(t)
    	if count1==count2:
            return True
    	else:
            return False

        
