class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mi = 0
        numset = set(nums)
        while mi in nums:
            mi+=1
        return mi
        