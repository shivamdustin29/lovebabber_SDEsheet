class Solution(object):
    def containsDuplicate(self, nums):
            temp = set(nums)
            if len(nums) == len(temp):
                return False
            else:
                return True

        
