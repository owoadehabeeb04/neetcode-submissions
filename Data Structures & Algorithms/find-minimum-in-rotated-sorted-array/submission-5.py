class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        lengthOfNums = len(nums)
        r = len(nums)-1
        minimumNumber = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                minimumNumber = min(minimumNumber, nums[l])
                break
            
            mid = (l+r) // 2
            minimumNumber = min(minimumNumber, nums[mid])
            if nums[mid] >= nums[l]:
                l =mid + 1
            else:
                r =mid - 1
        return minimumNumber

