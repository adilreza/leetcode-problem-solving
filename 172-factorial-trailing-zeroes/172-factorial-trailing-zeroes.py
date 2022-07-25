class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = 5
        count_zero = 0;
        for i in range(five, n+1, five):
            op = i
            while op % 5 == 0 and op >= 5:
                count_zero = count_zero + 1
                op = op//5
        return count_zero