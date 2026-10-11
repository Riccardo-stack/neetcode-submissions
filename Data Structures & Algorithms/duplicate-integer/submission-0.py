class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ins = set()
        for i in nums:
            if i in ins:
                return True
            else:
                ins.add(i)
        
        return False