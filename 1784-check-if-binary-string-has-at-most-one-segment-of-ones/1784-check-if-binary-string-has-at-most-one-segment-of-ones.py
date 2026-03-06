class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count=0
        for i in range(1,len(s)):
            if s[i]=='1' and s[i-1]=='0':
                count+=1
        return count==0
        