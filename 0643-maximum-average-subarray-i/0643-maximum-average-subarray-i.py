class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r = len(nums)
        l = 0
        temp = 0
        ans = float('-inf')
        for i in range(r):
            temp+=nums[i]
            if i -l ==k:
                temp-=nums[l]
                l+=1
            if i-l+1 == k:
                ans = max(ans,temp)
        return ans/k