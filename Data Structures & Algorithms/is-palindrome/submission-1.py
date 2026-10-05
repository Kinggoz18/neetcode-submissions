class Solution:
    def isValidNum(self, num: int) -> bool:
        try:
            float(num)
            return True
        except ValueError:
            return False

    def isPalindrome(self, s: str) -> bool:
        s2 = list(s.lower())
        s1 = list(s.lower())

        # Filter out none-characters
        s2Cleaned = [char for char in s2 if char.isalpha() or self.isValidNum(char)]
        s1Cleaned = [char for char in s1 if char.isalpha() or self.isValidNum(char)]
        x = len(s2Cleaned) - 1

        for i in range(len(s2Cleaned)):
            if s1Cleaned[i] != s2Cleaned[x]:
                return False
            x -= 1

        return True
