"""
Computers are spaced along a single row. An analysis is performed in the following way:
Choose a contiguous segment of a certain number of computers, starting from the beginning of the row. Analyze the available hard disk
space on each of the computers. Determine the minimum available disk space within this segment. After performing these steps for the
first segment, it is then repeated for the next segment, continuing this procedure until the end of the row
(i.e. if the segment size is 4, computers 1 to 4 would be analyzed, then 2 to 5 etc.)

Given this analysis procedure, write an algorithm to find the maximum available disk space among all the minima that are found during the analysis.

Input:
numComputer: an integer representing the number of computers
hardDiskSpace: a list of integers representing the hard disk space of the computers
segmentLength: an integer representing the length of contiguous segment of computers to be considered in each iteration

Output:
Return an integer representing the maximum available disk space among all the minima that are found during the analysis

Example 1:
    Input:
    numComputer = 3
    hardDiskSpace = [8,2,4]
    segmentLength = 2
    Output:
    2
    Explanation:
    In this array of computers, the subarrays of size 2 are [8,2] and [2,4]. Thus, the initial analysis returns 2 and 2 because those are the
    minima for the segments. Finally, the maximum of these values is 2.
TestCase 1:
    Input:
    5
    [1,2,3,1,2]
    1
    Output:
    3
    Explanation:
    The segment length is 1, so possible segments of computers are [1],[2],[3],[1], and [2]. The maximum of these segments is 3.
TestCase 2:
    Input:
    8
    [10,20,30,40,25,81,98,45]
    8
    Output:
    10
    Explanation:
    The segment length is equal to the number of computers, so the minimum value from the segment is 10. Since there are no other segments, the maximum value is 10.
"""

def maxOfAllMin(numComputer, hardDiskSpace, segmentLength):
    l,r = 0,0
    subst = hardDiskSpace[:segmentLength]
    minSpace = min(subst)
    r = segmentLength - 1

    while l < len(hardDiskSpace) - 1 and r < len(hardDiskSpace) - 1:
        toRemove = hardDiskSpace[l]
        l += 1
        r += 1
        if toRemove <= minSpace:
            ans = hardDiskSpace[l:r+1]
            minSpace = max(minSpace, min(ans))
        else:
            ans = min(minSpace, hardDiskSpace[r])
            minSpace = max(minSpace, ans)

    return minSpace
