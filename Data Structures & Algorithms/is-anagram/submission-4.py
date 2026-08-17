class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # arrayToCheck = []
        if len(s) != len(t):
            return False
        # for (i, firstString) in enumerate(s):
        #     for (j, secondString) in enumerate(t):
        #         if j not in arrayToCheck:
        #             if firstString == secondString:
        #                 arrayToCheck.append(j)
        #                 break
        # print(arrayToCheck)
        # if len(arrayToCheck) == len(t):
        #     return True
        # else:
        #     return False

        hashMapS = {}
        hashMapT = {}

        for (i, string) in enumerate(s):
            hashMapS[s[i]] = 1 + hashMapS.get(s[i], 0)
            hashMapT[t[i]] = 1 + hashMapT.get(t[i], 0)
        if hashMapS == hashMapT:
            return True
        else: 
            return False







