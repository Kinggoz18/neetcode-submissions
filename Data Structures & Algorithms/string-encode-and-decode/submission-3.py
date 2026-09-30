class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for word in strs:
            for ch in word:
                encodedChr = str(ord(ch)) + "#"
                encodedStr = encodedStr + encodedChr
            wordLen = len(word)
            encodedStr = encodedStr + "|"
        return encodedStr

    def decode(self, s: str) -> List[str]:
        words = list()
        i = 0
        encodedWrd = ""
        decodedStr = ""
        while i < len(s):
            # A single character
            while (True and i < len(s)) and (s[i] != "#" and s[i] != "|"):
                encodedWrd = encodedWrd + str(s[i])
                i += 1

            # The end of the word
            if s[i] == "|":
                print(encodedWrd)
                words.append(decodedStr)
                encodedWrd = ""
                decodedStr = ""
            else:
                # decode the character
                decodedStr = decodedStr + chr(int(encodedWrd))
                encodedWrd = ""
            i += 1

        return words
