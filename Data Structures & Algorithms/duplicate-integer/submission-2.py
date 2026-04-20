class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # 创建一个空的哈希集合
        
        for num in nums:
            if num in seen:  # 查字典：这个数字我之前见过吗？
                return True  # 见过！直接返回 True
            seen.add(num)    # 没见过，把它记在小本本上
            
        return False # 全都查完了也没重复，返回 False