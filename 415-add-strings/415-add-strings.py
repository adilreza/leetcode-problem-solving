class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l1>l2:
            zero_count = (l1-l2)
            num2 = "0"*zero_count + num2
        if l1<l2:
            zero_count = (l2-l1)
            num1 = "0"*zero_count + num1
        l1=l2=len(num1)
        c = 0
        result = ""
        l1 = l1-1
        while l1!=-1:
            tmp = 0
            a = int(num1[l1])
            b = int(num2[l1])
            if (a+b+c)>9:
                tmp = (a+b+c)%10
                result = result + str(tmp)
                c = 1
            else: 
                result = result + str(a+b+c)
                c=0
            l1 = l1-1
        if c==1:
            result = result+"1"
        fresult = result[::-1]
        return fresult
            
            
        