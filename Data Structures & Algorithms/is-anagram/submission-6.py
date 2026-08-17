class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMapS = {}
        for firstString in s:
            if firstString not in hashMapS:
                hashMapS[firstString] = 1
            else:
                hashMapS[firstString] = 1 + hashMapS[firstString]
        
        hashMapT = {}
        for secondString in t:
            if secondString not in hashMapT:
                hashMapT[secondString] = 1
            else:
                hashMapT[secondString] = 1 + hashMapT[secondString]
        
        if hashMapS == hashMapT:
            return True
        else:
            return False
        

            

