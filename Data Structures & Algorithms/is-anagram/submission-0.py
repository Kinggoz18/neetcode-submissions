class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Not the same length
        if len(s) != len(t):
            return False

        records_s = dict()
        records_t = dict()

        for x in range(len(s)):
            # Record the first word
            if records_s.get(s[x]):
                records_s[s[x]] += 1
            else:
                records_s[s[x]] = 1

            # Record the second word
            if records_t.get(t[x]):
                records_t[t[x]] += 1
            else:
                records_t[t[x]] = 1

        for x in range(len(s)):
            if records_s.get(s[x]) and records_t.get(s[x]):
                if records_s[s[x]] != records_t[s[x]]:
                    return False
            else:
                return False

        return True
