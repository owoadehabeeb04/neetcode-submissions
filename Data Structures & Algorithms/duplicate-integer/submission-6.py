class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        firstComparison= len(nums)
        secondComparison= len(set(nums))
        if firstComparison == secondComparison:
            return False
        else:
            return True 
        # for i in range(len(nums)):
        #     # this prints the index of each number

        #     for j in range(i+1, len(nums)):

        #         if nums[i] == nums[j]:
        #             return True
        # return False



        
