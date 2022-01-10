class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = len(a)
        l2 = len(b)
        if l1>l2:
            str = ""
            for i in range(l1-l2):
                str = str+"0"
            b = str+b
        if l1<l2:
            str = ""
            for i in range(l2-l1):
                str = str+"0"
            a = str+a

        c = False
        l = len(a)
        sum = ""
        for i in range(l):
            temp = int(a[l-1-i])+int(b[l-1-i])
            if temp==0:
                if c==True:
                    sum = sum+"1"
                    c=False
                else:
                    sum = sum+"0"
                    c = False
            elif temp==1:
                if c==True:
                    sum = sum+"0"
                    c=True
                else:
                    sum = sum+"1"
                    c = False
            elif temp==2:
                if c==True:
                    sum = sum+"1"
                    c=True
                else:
                    sum = sum+"0"
                    c = True
        if c==True:
            sum = sum+"1"

        sum = sum[::-1]
        return sum