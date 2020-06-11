"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

class Solution(object):
    def is_subset(self, intv1, intv2):
        #((interval[0] <= newInter1) or (interval[1] > newInter2) and (interval[0] < newInter1))
        if(intv1[0] <= intv2[0]) or (intv1[1] > intv2[1] and intv1[0] < intv2[0]):
            return True
        return False

    def is_subset_real(self, intv1, intv2):
        return self.helper_is_subset_real(intv1, intv2) or self.helper_is_subset_real(intv2, intv1)

    def helper_is_subset_real(self, intv1, intv2):
        case1 = intv1[0] >= intv2[0] and intv2[1] >= intv1[0] and intv1[1] >= intv2[1]
        case2 = intv1[0] <= intv2[0] and intv1[1] >= intv2[1]
        case3 = intv2[0] >= intv1[0] and intv1[1] >= intv2[0] and intv2[1] >= intv1[1]

        return case1 or case2 or case3

    def addValues(self, interval, lst):
        for i in range(interval[0], interval[1]):
                lst.add(i)
    def insertRange(self, interval_range, coupled_lst, ret_lst):


        minVal = min(interval_range)
        hasMin = True

        actualMin = min(min(interval_range),min(coupled_lst + [float('inf')]))
        if actualMin < minVal:
            hasMin = False


        for k in range(actualMin, max(interval_range)+1):
            if hasMin:
                if k not in interval_range:
                    ret_lst.append([minVal, k])
                    hasMin = False
            else:
                if k in interval_range:
                    minVal = k
                    hasMin = True
                else:
                    if k in coupled_lst:
                        ret_lst.append([k, k])

        if hasMin:
            ret_lst.append([minVal, max(interval_range)+1])

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        interval_range = set([])
        ret_lst = []
        coupled_lst = []


        newInter1 = newInterval[0]
        newInter2 = newInterval[1]
        added = False
        inputted = False
        outOfRange = False
        found = False

        if(newInterval[1]-newInterval[0] == 0):
                coupled_lst.append(newInterval[0])
        k = 0

        while k < len(intervals):
            interval = intervals[k]
            if(interval[1]-interval[0] == 0 and self.is_subset_real(interval, newInterval)):
                coupled_lst.append(interval[0])


            if(self.is_subset_real(interval, newInterval)):
                self.addValues(interval, interval_range)
                if not added:
                    self.addValues(newInterval, interval_range)
                    added = True
                found = True
            elif (found and added and inputted) or (not added and not inputted):
                ret_lst.append([interval[0], interval[1]])
                print(interval[0], " ", interval[1], " is ", self.is_subset_real(interval, newInterval))
                if found:
                    outOfRange = True
            elif found or (outOfRange and added and not inputted):
                self.insertRange(interval_range, coupled_lst, ret_lst)
                k -= 1
                inputted = True

            else:
                print(found, added, inputted)
                print(interval[0], " ", interval[1])
            k += 1



        if not added:
            if(len(interval_range) == 0) and len(coupled_lst) != 0:

                item = coupled_lst[0]
                for i in range(len(ret_lst)):
                    if ret_lst[i][0] > item:
                        ret_lst.insert(i, [item, item])
                        return ret_lst
                ret_lst.append([item, item])
            elif (len(interval_range) == 0) and len(coupled_lst) == 0:
                print("ok buddy")
                item = newInterval[0]
                for i in range(len(ret_lst)):
                    if ret_lst[i][0] > item:
                        ret_lst.insert(i, [newInterval[0], newInterval[1]])
                        return ret_lst
                ret_lst.append([newInterval[0], newInterval[1]])
            else:
                print(len(interval_range), " ", len(coupled_lst))
                self.addValues(newInterval, interval_range)
                added = True
                self.insertRange(interval_range, coupled_lst, ret_lst)
        elif not inputted:
            self.insertRange(interval_range, coupled_lst, ret_lst)




        return ret_lst
