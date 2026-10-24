class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s,best=set(nums),0
        for i in s:
            if i-1 not in s:
                y=i
                while y+1 in s:
                    y+=1
                best=max(best,y-i+1)
        return best