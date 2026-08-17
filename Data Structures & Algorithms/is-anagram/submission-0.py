class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # brute force approach 
        stringS = ''.join(sorted(s))
        stringT = ''.join(sorted(t))
        print(stringS, stringT)

        if stringS == stringT:
            return True
        else:
            return False