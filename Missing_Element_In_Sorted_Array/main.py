"""
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.

Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Note:

    1 <= A.length <= 50000
    1 <= A[i] <= 1e7
    1 <= K <= 1e8
"""
class Solution(object):
    def missingNumber(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """

        p = nums[0]
        count = 0
        for i in range(1, len(nums)):
            num = nums[i]
            if num == p + 1:
                p += 1
            else:
                while p < num -1:
                    count += 1
                    p += 1
                    if count == k:
                        return p
                p += 1

        return p + k - count

def testcase(method, input, sol):
    test_sol = method(*input)
    try:
        assert (
            test_sol == sol
        )
        print("Test Case: (PASS) ", *input, "->", sol)
    except:
        print("Test Case: (FAIL) Expected:", sol, " Actual:", method(*input))


if __name__ == "__main__":
    S = Solution()


    testcase(S.missingNumber, [[4,7,9,10],1], 5)
    testcase(S.missingNumber, [[4,7,9,10],3], 8)
    testcase(S.missingNumber, [[1,2,4],3], 6)

    print("All Test Cases Passed")
