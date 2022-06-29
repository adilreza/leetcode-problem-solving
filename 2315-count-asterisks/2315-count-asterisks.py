class Solution:
    def countAsterisks(self, s: str) -> int:
        l = len(s)
        pair = 0
        result = 0
        for i in range(l):
            if s[i]=="|":
                pair = pair + 1
            if pair%2==0 and s[i]=="*":
                result = result+1
        return result