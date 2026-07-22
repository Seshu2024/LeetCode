class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_arr = list(map(lambda x:x*x,nums))
        return sorted(new_arr)