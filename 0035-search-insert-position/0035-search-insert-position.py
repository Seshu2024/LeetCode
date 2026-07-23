class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            # print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1

        if nums[mid] != target:
                nums.append(target)
                nums.sort()
        return nums.index(target)
        