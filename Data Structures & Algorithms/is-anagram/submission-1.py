class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # # brute force approach 
        # stringS = ''.join(sorted(s))
        # stringT = ''.join(sorted(t))
        # print(stringS, stringT)

        # if stringS == stringT:
        #     return True
        # else:
        #     return False


        # to optimize to o(n)
        tCount = {}
        sCount = {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        print(sCount, tCount)
        if sCount == tCount:
            return True
        else:
            return False
