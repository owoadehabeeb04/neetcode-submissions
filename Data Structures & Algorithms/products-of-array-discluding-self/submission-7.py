class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = [0] * len(nums)
        postFixArray = [0] * len(nums)
        outputArray = [0] * len(nums)
        n = len(nums)
        prefixArray[0] = postFixArray[n - 1] = 1

        for i in range(1, len(nums)):
            prefixArray[i] = nums[i -1] * prefixArray[i - 1]
        for i in range(len(nums)-2, -1, -1):
            postFixArray[i] = nums[i + 1] * postFixArray[i + 1]
 
        for i in range(len(nums)):
            outputArray[i] = prefixArray[i] * postFixArray[i] 
        return outputArray


