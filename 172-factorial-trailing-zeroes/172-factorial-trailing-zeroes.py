class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n<5:
            return 0
        c=n//5+n//25+n//125+n//625+n//3125
        return c