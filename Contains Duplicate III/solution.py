class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        a = {}
        for i in range(len(nums)):
            if nums[i] in a:
                
                if (i - a[nums[i]]) <= indexDiff and abs(nums[i] - nums[a[nums[i]]]) <= valueDiff:
                    return True
            a[nums[i]] = i
        return False
    
s = Solution()

print(s.containsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15], 1, 3))