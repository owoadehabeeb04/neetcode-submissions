class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroup = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))

            if sortedWord not in anagramGroup:
                anagramGroup[sortedWord] = []

            anagramGroup[sortedWord].append(word)

        return list(anagramGroup.values())        