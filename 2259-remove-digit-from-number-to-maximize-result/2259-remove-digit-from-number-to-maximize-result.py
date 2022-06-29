class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        digit = str(digit)
        number = str(number)
        l = len(number)
        selector = -5
        for i in range(l):
            if number[i]==digit:
                selector = i
                if i+1!=l:
                    if int(number[i+1]) > int(number[i]):
                        selector = i
                        break
        return number[0:selector]+number[selector+1:l]