class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for (i, num) in enumerate(nums):
            for (j, num2) in enumerate(nums):
                if i != j:
                    if nums[i] == nums[j]:
                        return True
        return False
    
       