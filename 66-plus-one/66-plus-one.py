class Solution(object):
    def plusOne(self, digits):
        l = len(digits)
        carry = 0
        for i in range(l,0,-1):
            temp = digits[i-1]+1
            if temp<=9:
                digits[i-1] = digits[i-1]+1
                carry = 0
                break;
            else:
                digits[i-1] = 0;
                carry = 1
        if carry == 1:
            digits =[1]+digits
        return digits
        