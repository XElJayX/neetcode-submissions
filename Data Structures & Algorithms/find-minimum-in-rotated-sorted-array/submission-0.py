class Solution:
    def findMin(self, nums: List[int]) -> int:
        k = nums[0]
        for num in nums:
            if num < k:
                k = num
        return k
            