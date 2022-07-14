class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=nums[0]
        life =0
        n=len(nums)
        for i in range(n):
            if (nums[i]==candidate):
                life+=1
            elif (life==0):
                candidate=nums[i]
                life=1
            else:
                life-=1
                
        return candidate 
