class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        cur=0
        for i in range(len(heights)):
            cur=heights[i]
            for l in range(i-1,-1,-1):
                if  heights[l]>=heights[i]:
                    cur+=heights[i]
                else:
                    break
            for r in range(i+1,len(heights)):
                if  heights[r]>=heights[i]:
                    cur+=heights[i]
                else:
                    break   
            print(cur)  
            res=max(res,cur)
        return res         
                