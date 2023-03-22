class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        a = {}
        for i in range(len(nums)):
            if nums[i] in a:
                if (i - a[nums[i]]) <= k:
                    return True
            a[nums[i]] = i
        return False

