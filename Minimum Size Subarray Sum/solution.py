class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start=0
        end=0
        current_sum=0
        min_length = -1
        
        while end < len(nums):
            current_sum = current_sum + nums[end]
            end += 1
            
            while start < end and current_sum >= target:
                current_sum -= nums[start]
                start += 1
                
                min_length = end - start + 1 if min_length < 0  else min(min_length, end - start + 1)
        
        return max(min_length, 0)