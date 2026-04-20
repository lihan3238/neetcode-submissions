class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cur=1
        res=1
        if not len(nums):
            return 0
        nums.sort()
        last=nums[0]
        print(nums)
        for i in nums[1:]:
            if i==last+1:
                cur+=1
                res=res if res>cur else cur
            elif i != last:
                cur=1
            last=i 
        return res