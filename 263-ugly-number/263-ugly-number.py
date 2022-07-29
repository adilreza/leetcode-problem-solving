class Solution:
    def isUgly(self, n: int) -> bool:
        prime = [2, 3, 5]
        if n == 0:
            return False
        else:
            num = n
            while num % prime[0] == 0 or num % prime[1] == 0 or num % prime[2] == 0:
                if num % prime[0] == 0:
                    num = num / prime[0]
                if num % prime[1] == 0:
                    num = num / prime[1]
                if num % prime[2] == 0:
                    num = num / prime[2]
            if num == 1:
                return True
            else:
                return False