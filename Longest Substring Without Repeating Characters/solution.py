class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = 0
        longest_size, current_size = 0, 0
        occurence_count = {}

        while index < len(s):
            if s[index] in occurence_count:
                index = occurence_count[s[index]] + 1
                occurence_count.clear()
                longest_size = max(longest_size, current_size)
                current_size = 0
            else:
                occurence_count[s[index]] = index
                index += 1
                current_size += 1

        longest_size = max(longest_size, current_size)
        
        return longest_size