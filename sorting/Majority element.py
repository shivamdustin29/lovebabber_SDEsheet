class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorElem = 0
        for num in nums:
            if not count:
                count = 1
                majorElem = num
            else:
                if num == majorElem:
                    count += 1
                else:
                    count -= 1
        return majorElem
       **************************************By using Counter**********************
        class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        
