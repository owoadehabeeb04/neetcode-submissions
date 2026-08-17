class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    

        # for i, num in enumerate(nums):
        #     for j, num2 in enumerate(nums):
        #         if i != j:
        #             if num + num2 == target:
        #                 return [i, j]

        # key will be the numbers in the array, then the index will bethe values in the array 
        # {3: 0, 4: 1, 5: 2, 6: 3}. target = 7 
        # subtarct 7 from 3 it will give us thenwe search fpr 4 in the hashmap or the keys or dictionary
        # 

        hashMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashMap:
                return [hashMap[complement], i]                
            hashMap[nums[i]] = i

































        