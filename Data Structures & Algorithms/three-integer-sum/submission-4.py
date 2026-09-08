class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(0,n):
            target = -1 * nums[i]
            start = i+1
            end = n-1
            while(start<end):
                if nums[start]+nums[end] > target :
                    end-=1
                elif (nums[start]+nums[end]) < target :
                    start += 1
                else:
                    res.add((nums[i], nums[start], nums[end]))
                    start+=1
                    end-=1
        return [list(t) for t in res]