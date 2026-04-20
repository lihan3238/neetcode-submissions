class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                b=nums.index(target-nums[i])
                if i<b:
                    return [i,b]
                if i>b:
                    return [b,i]