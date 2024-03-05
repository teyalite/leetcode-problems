class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return False
        
        j = 0

        for i in range(len(t)):
            if t[i] == s[j]:
                j+=1
            
            if j == len(s):
                return True
            
        return False
    
s = Solution()