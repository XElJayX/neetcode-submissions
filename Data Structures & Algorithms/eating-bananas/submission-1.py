class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1

        while low < high:
            mid = (low+high)//2

            total = sum(math.ceil(x/mid) for x in piles)

            if total <= h :
                high = mid
            else:
                low = mid + 1
        return low

        