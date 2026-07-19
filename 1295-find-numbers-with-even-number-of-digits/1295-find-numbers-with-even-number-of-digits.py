class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            x = str(i)
            if len(x) >1 and len(x)%2==0:
                count+=1
        return count