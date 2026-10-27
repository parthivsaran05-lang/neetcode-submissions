class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,val in enumerate(nums):
            comple=target-val
            if comple in seen:
                return [seen[comple],i]
            seen[val]=i