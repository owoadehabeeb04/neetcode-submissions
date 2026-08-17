class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        lengthOfNums = len(nums)
        minimumNumber = nums[0]
        while l < lengthOfNums - 1:
            if nums[l] > nums[l + 1]:
                minimumNumber = nums[l + 1]
                return minimumNumber
            elif nums[l] < nums[l + 1]:
                l = l + 1
                minimumNumber = nums[l]
        return nums[0]
            

