class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_appeared = set()

        for i in nums:
            if i in has_appeared:
                return True
            else:
                has_appeared.add(i)
        
        return False
