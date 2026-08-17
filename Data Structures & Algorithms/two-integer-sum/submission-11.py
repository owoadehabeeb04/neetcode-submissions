class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment not in hashMap:
                hashMap[num] = i
            else:
                return [hashMap[compliment], i]


