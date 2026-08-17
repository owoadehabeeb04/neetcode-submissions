import string


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # alphabetStrs = list(string.ascii_lowercase)
        # alphabetObj = {}
        # for i, alphabet in enumerate(alphabetStrs):
        #     alphabetObj[alphabet] = i + 1
        # hashMap = {}
        # for str in strs:
        #     arrayToPutInHashMap = []
        #     for s in str:
        #         arrayToPutInHashMap.append(alphabetObj[s])
        #         arrayToPutInHashMap.sort()
        #     hashMap[str] = arrayToPutInHashMap
        # finalGrouped = {}
        # for key, value in hashMap.items():
        #     val_tuple = tuple(value)
        #     if val_tuple not in finalGrouped:
        #         finalGrouped[val_tuple] = []
    
        #         finalGrouped[val_tuple].append(key)

        # result = finalGrouped.values()
        # print(result)
        res = defaultdict(list)
        print(res)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            print(count)
            res[tuple(count)].append(s)
        return list(res.values())
        


