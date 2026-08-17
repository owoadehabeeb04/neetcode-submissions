from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        res = []

        for num in nums:
            if num in hashMap:
                hashMap[num] =1 + hashMap[num]
            else:
                hashMap[num] = 1
        
        arrayToCheckFrom = list(hashMap.values())
        arrayToCheckFrom.sort(reverse = True)
        top_k_frequencies = arrayToCheckFrom[:k]
        print(top_k_frequencies)
        for key, value in hashMap.items():
            
            if value in top_k_frequencies:
                res.append(key)
            if len(res) == k:
                break
        return res

        

            
            

            
                

        



