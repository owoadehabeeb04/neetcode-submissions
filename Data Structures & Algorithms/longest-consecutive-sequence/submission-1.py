class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # pointer = 0
        # if nums=[]:
        #     return pointer
        # nums.sort()
        # for i in range(len(nums)):
        #     print(nums)
        #     if i < len(nums)-1:
        #         print('checckck')
        #         if nums[i]  ==  nums[i + 1]:
        #             print('check')
        #             continue
        #             # to check consecutive 
        #         if nums[i + 1] != nums[i] + 1:
        #             continue 
        #     pointer += 1
        # return pointer

        numbers = set(nums)
        lengthOfLongest = 0

        for num in numbers:

            if num - 1 not in numbers:
                length = 1

                while num + length in numbers:
                    length = length + 1
                lengthOfLongest = max(lengthOfLongest, length)
        return lengthOfLongest
                



