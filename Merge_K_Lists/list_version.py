# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        rtn_lst = []
        index_lst = [0]*len(lists)
        continue_ = True
        while continue_:
            continue_ = False
            minIndex,minVal = None, float("inf")
            for i,l in enumerate(lists):
                if index_lst[i] < len(l):
                    continue_ = True
                    val = l[index_lst[i]]
                    if val < minVal:
                        if minIndex is not None:
                            temp = minIndex
                            minIndex = i
                            minVal = val
                            index_lst[i] += 1
                            index_lst[temp] -= 1
                        else:
                            minIndex = i
                            minVal = val
                            index_lst[i] += 1
            if minIndex is not None:
                rtn_lst.append(minVal)

        return rtn_lst

if __name__ == "__main__":

    sol = Solution()
    t = [[1,4,5],[1,3,4],[2,6]]
    print(sol.mergeKLists(t))
