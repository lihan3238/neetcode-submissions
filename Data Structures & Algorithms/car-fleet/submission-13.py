class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res=0
        fleet=[]
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)
        for i in range(len(position)):
            f=0
            for j in range(i):
                if j in fleet:
                    continue
                if (target-pair[j][0])/pair[j][1] >= (target-pair[i][0])/pair[i][1] :
                    f=1

                    fleet.append(i)
                    print(i,"catch up",j)
                    break;
            if f!=1:
                print(i)
                res+=1
        return res
                
