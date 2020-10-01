"""
    Given 2 lists of meetings where each list corresponds to the meetings a person has in a day,
    return a list of meetings that give the free meeting times that 2 people can have.
"""

class Solution():

    def compare(self,t1,t2):
        #9:00, 10:00

        c1 = t1.index(":") #1
        c2 = t2.index(":") #2

        d1_hour = int(t1[:c1])
        d2_hour = int(t2[:c2])


        if d1_hour < d2_hour:
            return -1
        elif d1_hour > d2_hour:
            return 1
        else:
            d1_min = int(t1[c1+1:])
            d2_min = int(t2[c2+1:])
            if d1_min < d2_min:
                return -1
            elif d1_min > d2_min:
                return 1
            else:
                return 0

    def twoIntervalOverlap(self, time1, time2, i, j):
        #Cases for no calculateOverlap
            #last element of the first is < first element of last
            #last element of the last is < first element of first

        newtimeInterval = []

        first_case = self.compare(time1[1], time2[0])
        second_case = self.compare(time2[1], time1[0])
        third_case = self.compare(time1[1], time2[1])


        if first_case < 0:
            #if first_case == 0:
            #    j += 1
            return True, [time1[1], time2[0]], i+1, j
        elif second_case < 0:
            #if second_case == 0:
            #    i += 1
            return True, [time2[1], time1[0]], i, j+1
        else:
            if third_case > 0:
                j += 1
            elif third_case < 0:
                i += 1
            else:
                i+=1
                j+=1
            return False, [], i, j

    def withinBounds(self, interval, restriction1, restriction2):

        return self.compare(interval[0], restriction1[0]) >= 0 and self.compare(interval[0], restriction2[0]) >=0 \
        and self.compare(interval[1], restriction1[1]) <= 0 and self.compare(interval[1], restriction2[1]) <= 0

    def flatten(self, lst1, dailyBound):
        new_lst = [["0:00", dailyBound[0]]]
        i = 0
        while i < len(lst1):
            if i <len(lst1) and i+1 < len(lst1) and lst1[i][1] == lst1[i+1][0]:
                new_lst.append([lst1[i][0], lst1[i+1][1]])
                i += 1
            else:
                new_lst.append(lst1[i])
            i += 1
        new_lst.append([dailyBound[1], "24:00"])
        return new_lst

    def calculateOverlap(self, lst1, dailyBound1, lst2, dailyBound2, meetingLength):

        lst1 = self.flatten(lst1, dailyBound1)
        lst2 = self.flatten(lst2, dailyBound2)


        rtn_lst = []
        i, j = 0,0

        while i < len(lst1) and j < len(lst2):

            first_time = lst1[i]
            second_time = lst2[j]

            succ, overlap, i,j = self.twoIntervalOverlap(first_time, second_time, i, j)
            if succ:
                rtn_lst.append(overlap)

        return rtn_lst

if __name__ == "__main__":
    sol = Solution()
    testcase1 = [[["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]], ["9:00", "20:00"], \
                  [["10:00", "11:30"], ["12:30","14:30"], ["14:30", "15:00"], ["16:00", "17:00"]], \
                  ["10:00", "18:30"], 30]


    print(sol.calculateOverlap(testcase1[0],testcase1[1], testcase1[2], testcase1[3], testcase1[4]))
