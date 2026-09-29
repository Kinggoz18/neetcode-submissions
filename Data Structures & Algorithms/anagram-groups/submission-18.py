class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary of letters a-z
        az = "abcdefghijklmnopqrstuvwxyz"
        azDict = {}
        for i in range(len(az)):
            azDict[az[i]] = i
        
        solution = defaultdict(list)
        # Create a dictionary of key value pair
        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[azDict[ch]] += 1 # count each letters occurance in the word
            solution[tuple(counts)].append(word)
        
        return list(solution.values())

