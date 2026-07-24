class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        maxii = max(piles)

        while low <= maxii :
            mid = (low + maxii) // 2
            hours = 0
            for p in piles:
                hours += (p + mid -1) // mid

            if hours <= h:
                maxii = mid-1
            else:
                low = mid+1
        return low