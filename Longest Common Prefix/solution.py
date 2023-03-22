class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = min(strs, key=lambda s: len(s))

        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[0:i]
                
        return shortest