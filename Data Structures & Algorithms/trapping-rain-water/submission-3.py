class Solution:
    def trap(self, height: List[int]) -> int:
        f=1
        h=0
        cur=0
        row=0
        res=0
        while(f):
            f=0
            h+=1
            row=0
            for i in range(len(height)):
                if height[i]<h:
                    if i==0 or i==len(height)-1:
                        print("h:",h,"i:",i,"end step")
                        continue
                    else:
                        if height[i-1]>=h:
                            print("h:",h,"i:",i,"empty")
                            while height[i]<h:
                                if i == len(height)-1 :
                                    cur=0
                                    break
                                cur+=1
                                i+=1
                            row+=cur
                            cur=0
                            print("-\n",i)
                else:
                    f=1
            res+=row
        return res





        