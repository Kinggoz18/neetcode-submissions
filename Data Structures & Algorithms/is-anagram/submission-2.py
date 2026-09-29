class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Not the same length
        if len(s) != len(t):
            return False

        records_s = dict()
        records_t = dict()

        # record the letters for string s and t
        for i in range(len(s)):
            if s[i] not in records_s:
                records_s[s[i]] = 1
            else:
                records_s[s[i]] += 1

            if t[i] not in records_t:
                records_t[t[i]] = 1
            else:
                records_t[t[i]] += 1
            
        # check the letter count matches both
        for i in range(len(s)):
            if s[i] not in records_t or s[i] not in records_s:
                return False
            if records_t[s[i]]!= records_s[s[i]]:
                return False
        return True
