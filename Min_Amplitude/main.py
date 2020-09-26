import heapq
class Solution(object):

    def arr_max(self, arr):
        mi = float("inf")
        min_ind = 0
        for i in range(len(arr)):
            if arr[i] < mi:
                mi = arr[i]
                min_ind = i
        return mi, min_ind

    def arr_min(self, arr):
        mi = float("inf")
        min_ind = 0
        for i in range(len(arr)):
            if arr[i] < mi:
                mi = arr[i]
                min_ind = i
        return mi, min_ind

    def minAmp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[0,1,1,4,6,6,6]
        if len(nums) < 4:
            return 0
        nums.sort()

        res_1 = min(nums[-1]-nums[3],nums[-4]-nums[0]);
        res_2 = min(nums[-2]-nums[2],nums[-3]-nums[1]);


        return min(res_1, res_2)


if __name__ == "__main__":
    sol = Solution()

    testcases = [[-1,3,-1,8,5,4], [10,10,3,4,10]]
    for i, test in enumerate(testcases):
        print("Testcase " + str(i) + " is: " + str(sol.minAmp(test)))
