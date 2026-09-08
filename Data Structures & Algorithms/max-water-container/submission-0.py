class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        start = 0
        end = n-1
        area = 0
        while start < end:
            curr_area = (end-start)* min(heights[start],heights[end])
            area = max(area,curr_area)
            if heights[start] > heights[end]:
                end-=1
            else:
                start+=1
        return area