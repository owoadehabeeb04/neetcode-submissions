class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for n in nums:
            print(n)
            if n in hashMap:
                hashMap[n] =  1 + hashMap[n]
                return True
            else:
                hashMap[n] = 1
        return False 
       