class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,path=[],[]
        def bt(i):
            if i == len(nums):
                res.append(path[:])
                return
            path.append(nums[i])
            bt(i+1)
            path.pop()
            bt(i+1)
        bt(0)
        return res