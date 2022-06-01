class Solution:
    def missingNumber(self, nums: List[int]) -> int:
         return [el for el in set([x for x in range(0,len(nums)+1)]) ^ set(nums)][0]
        
