class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss,s=[],set(nums)
        for i in s:
            if i+1 not in s and (i+1)<=len(nums):
                miss.append(i+1)
            elif i-1 not in s and (i-1) >=0:
                miss.append(i-1)
        return min(miss)
            