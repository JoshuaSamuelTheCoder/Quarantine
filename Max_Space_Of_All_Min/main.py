"""
Choose a contiguous segment of a certain number of computers, starting from the beginning
of the row. Analyze the available hard diskspace on each of the computers. Determine the
minimum available disk space within this segment. After performing these steps for the first
segment, it is then repeated for the next segment, continuing this procedure until the end of the row
(ie if the segment size is 4 computers 1 to 4 would be analyzed, then 2 to 5 etc.)

Given this analysis, write an algorithm to find the maximum available disk space among all the minima
that are found during the analysis.

Input:
    numComputer: an integer representing the number of computers
    hardDiskSpace: a list of integers representing the hard disk space of the computers.
    segmentLength: an integer representing the length of contiguous segment of computers to be considered in each iterations.
Output:
    An integer representing the maximum available disk space among all the minima that are found during the analysis.

Constraints:
1 <= numComputer <= 10^6
1 <= segmentLength <= numComputer
1 <= hardDiskSpace[i] <= 10^9
0 <= i <= numComputer

Example:
Input:
    numComputer = 3
    hardDiskSpace = [8,2,4]
    segmentLength = 2
Output:
    2
Explantion:
In this array of computers, the subarrays of size 2 are [8,2] and [2,4]. Thus, the initial analysis returns 2 and 2 because those
are the minima for the segments. Finally, the maximum of these values is 2.

TestCase 1:
    Input:
    5, [1,2,3,1,2], 1
    Output:
    3
TestCase 2:
    Input:
    8, [10,20,30,40,25,81,98,45],8
    Output:
    10
"""
def maxOfAllMin(numComputer, hardDiskSpace, segmentLength):
    #WRITE YOUR CODE HERE
    l,r, = 0,0
    subst = hardDiskSpace[:segmentLength]
    minSpace = min(subst)
    r = segmentLength - 1

    while l < len(hardDiskSpace)-1 and r < len(hardDiskSpace)-1:
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
