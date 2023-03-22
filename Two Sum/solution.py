class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = []
        diff = {}
        
        for i in range(len(nums)):
            if nums[i]in diff:
                answer.append(diff[nums[i]])
                answer.append(i)
                break
            
            diff[target - nums[i]] = i
        
        return answer