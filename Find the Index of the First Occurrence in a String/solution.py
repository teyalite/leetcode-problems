class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1
        
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
            
        return -1
    
    def strRabinKarp(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        if haystack[0:len(needle)] == needle:
            return 0
        
        hash=0
        current_hash=0
        
        for i in range(0, len(needle)):
            hash += ord(needle[len(needle) - 1 - i]) * (256**i)
            current_hash += ord(haystack[len(needle) - 1 - i]) * (256**i)
        
        for index in range(len(needle), len(haystack)):

            current_hash-=(ord(haystack[index - len(needle)]) * 256**(len(needle) - 1))
            current_hash*=256
            current_hash+=ord(haystack[index])
            
            if current_hash == hash:
                k = 0
                
                while k < len(needle):
                    if needle[k] != haystack[k + index - len(needle) + 1]:
                        break
                    k += 1

                if k == len(needle):
                    return index - len(needle) + 1

        return -1
    