class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        while nums:
            i = 0
            first = nums.pop(0)
            
            for i in range(len(nums)):
                if nums[i] == first:
                    count += 1
        return count