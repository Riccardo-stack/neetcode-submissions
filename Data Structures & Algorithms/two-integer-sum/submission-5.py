class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for j in range(len(nums)):
            hashmap[nums[j]] = j
        
        for i in range(len(nums)):
            difference = (target - nums[i])
            if difference in hashmap and i != hashmap[difference]:
                return [i, hashmap[difference]]