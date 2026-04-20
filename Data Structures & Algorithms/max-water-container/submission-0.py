class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur=0
        res=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                cur=min(heights[i],heights[j])*(j-i)
                res = res if res>cur else cur
        return res

