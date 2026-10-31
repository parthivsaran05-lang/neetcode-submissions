# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res=[]
        cur=head
        while cur:
            group=[]
            for i in range(k):
                if not cur:
                    break
                group.append(cur)
                cur=cur.next
            res.append(group)
        res1=[]
        for i in res:
            if len(i)==k:
                i.reverse()
            for j in i:
                res1.append(j)
        for i in range(len(res1)-1):
            res1[i].next=res1[i+1]
        res1[-1].next=None
        return res1[0] if res1 else None