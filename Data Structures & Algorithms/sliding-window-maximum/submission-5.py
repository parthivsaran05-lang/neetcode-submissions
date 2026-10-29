class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxi = max(nums[:k])
        res.append(maxi)

        for i in range(1, len(nums) - k + 1):
            if nums[i + k - 1] > maxi:
                maxi = nums[i + k - 1]
            elif nums[i - 1] == maxi:
                maxi = max(nums[i:i+k])

            res.append(maxi)

        return res