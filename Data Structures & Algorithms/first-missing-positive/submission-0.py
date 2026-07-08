class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mi = 1 
        i = 0
        while i<len(nums):
            if mi not in nums:
                break
            mi+=1
            i+=1
        return mi