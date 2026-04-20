class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        t1=counts.most_common(k)
        t2=[]
        for i in t1:
            t2.append(i[0])
        return t2