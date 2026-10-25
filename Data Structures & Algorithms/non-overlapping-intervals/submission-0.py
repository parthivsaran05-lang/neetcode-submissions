class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        co=0
        res=[]
        intervals.sort(key=lambda i:i[0])
        for i in intervals:
            if not res or res[-1][1]<=i[0]:
                res.append(i)
            else:
                co+=1
                res[-1][1]=min(res[-1][1],i[1])
        return co