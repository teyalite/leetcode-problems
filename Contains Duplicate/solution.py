class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        occurences = {}

        for num in nums:
            if num in occurences:
                return True
            occurences[num] = 1
        
        return False