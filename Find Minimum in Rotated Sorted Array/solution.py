class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            m = left + int((right - left) / 2)

            if nums[m] < nums[right]:
                right = m
            else:
                left = m + 1

        return nums[left]
