class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        l=[-1]*len(heights)
        r=[len(heights)]*len(heights)
        stack=[]
        for i in range(len(heights)):
            if i==0:
                stack.append(i)
                continue
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if stack:
                l[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            if i==(len(heights)-1):
                r[len(heights)-1]=len(heights)
                stack.append(i)
                continue
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if stack:
                r[i]=stack[-1]
            stack.append(i)
        
        print(l,r)

        for i in range(len(heights)):
            res=max(res,heights[i]*(r[i]-l[i]-1))
        return res




                       