class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # firstComparison= len(nums)
        # secondComparison= len(set(nums))
        # if firstComparison == secondComparison:
        #     return False
        # else:
        #     return True 
        # for i in range(len(nums)):
        #     # this prints the index of each number

        #     for j in range(i+1, len(nums)):
        #         # then move forward to mprevent checking for the same index
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        hashMap = {}

        for n in nums:
            if n in hashMap:
                hashMap[n]= 1 + hashMap[n]
                return True
            else:
                hashMap[n]= 1
        return False




        



        
