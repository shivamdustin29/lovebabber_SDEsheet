************************method 1**********************
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c=Counter(nums)
        return(c.most_common()[0][0])

       
        ******************method 2*********************
        class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]

        
