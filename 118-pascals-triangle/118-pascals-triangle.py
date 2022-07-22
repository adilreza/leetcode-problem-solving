class Solution(object):
    def generate(self, numRows):
        result = [[1]]
        dp = [1]
        for i in range(numRows-1):
            dp.append(1)
            tmp=[]
            l = len(dp)
            for j in range(1,l-1):
                tmp.append(dp[j]+dp[j-1])
            tmp.append(1)
            tmp[:0]=[1]
            result.append(tmp[0:len(tmp)])
            dp = tmp
        return result
        