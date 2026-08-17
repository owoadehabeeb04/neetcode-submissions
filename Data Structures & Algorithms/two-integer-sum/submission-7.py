class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i, num in enumerate(nums):
        #     for j , num2 in enumerate(nums):
        #         if (num + num2) == target:
        #             return [i, j]
        # return -1

        # hashSet = {}        
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     print(hashSet)
        #     if complement in hashSet:
        #         return [hashSet[complement], i]  

        #     hashSet[nums[i]] = i

        # return []
        

        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    if num + num2 == target:
                        return [i, j]






























        