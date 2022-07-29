class Solution:
    def addDigits(self, num: int) -> int:
            if num<10:
                return num
            else:
                sum = 0;
                tnum = num
                while(tnum!=0):
                    sum = sum + tnum%10
                    tnum = tnum//10

                return self.addDigits(sum)