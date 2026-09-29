class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            solution[key].append(word)
        
        return list(solution.values())