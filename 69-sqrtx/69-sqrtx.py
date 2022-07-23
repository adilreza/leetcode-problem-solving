class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        l = 0
        h = x//2
        mid = (l+h)//2

        ans = -1
        while l<=h:
            square = mid * mid
            if square==x:
                return mid
            if square<x:
                ans = mid
                l = mid + 1
            elif square>x:
                h = mid-1
            mid = (l+h)//2
        return ans