class Solution:
    def mySqrt(self, x: int) -> int:
        cnt = 0;
        neg=1
        while x>0:
            x = x-neg;
            cnt = cnt+1
            neg = neg + 2
            if (x-neg)<0:
                break;
                
        
        return cnt