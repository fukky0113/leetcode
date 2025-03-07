class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left in range(len(nums)):
            for right in range(len(nums)-1, left, -1):
                if(nums[left] + nums[right] == target):
                    return [left, right]
