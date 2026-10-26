class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        for i,val in enumerate(nums):
            if i==k-1:
                return val