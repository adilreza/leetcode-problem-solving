class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = len(num)
        result = "0"
        for i in range(l-2):
            if num[i]==num[i+1]==num[i+2]:
                if int(num[i]+num[i+1]+num[i+2])>=int(result):
                    result = num[i]+num[i+1]+num[i+2]
        if result == "0":
            return ""
        else:
            return result