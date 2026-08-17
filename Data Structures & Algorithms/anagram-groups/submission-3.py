class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagram = {}

        for s in strs:
            sortedString = "".join(sorted(s))
            print(sortedString)
        
            if sortedString not in groupAnagram:
                groupAnagram[sortedString] = []
            groupAnagram[sortedString].append(s)
        print(groupAnagram)
        
        return list(groupAnagram.values())


       





        

