class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        arrayToReturn = []
        for i, num in enumerate(nums):
            print(i, num)
            compliment = target - num
            print(compliment)
            if compliment not in hashMap:
                hashMap[num] = i
                print(hashMap)
             
            else:
                arrayToReturn.append(hashMap[compliment])
                arrayToReturn.append(i)
                return arrayToReturn


