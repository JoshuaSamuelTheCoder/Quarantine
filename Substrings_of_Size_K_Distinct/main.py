
class Solution(object):


    def sol(self, st, k):
        """
        :type st: str
        :type k: int
        :rtype: List[str]
        """
        ans_lst = []
        count = {}
        l, r = 0,0
        while(r < len(st)):
            count[st[r]] = count.get(st[r], 0) + 1
            if len(count.keys()) == k:
                break
            r += 1

        while(l < len(st)):
            if len(count.keys()) < k:
                r += 1
                if r == len(st):
                    break
                count[st[r]] = count.get(st[r], 0) + 1

            else:
                if r - l + 1 == k:
                    ans = st[l:r+1]
                    if ans not in ans_lst:
                        ans_lst.append(ans)
                count[st[l]] -= 1
                if count[st[l]] == 0:
                    del count[st[l]]
                l += 1
        return ans_lst


if __name__ == "__main__":
    s = Solution()

    testcases = [["abcabc", 3], ["abacab", 3], ["awaglknagawunagwkwagl", 4]]
    for i, test in enumerate(testcases):
        print("Testcase " + str(i) + " is: " + str(s.sol(test[0], test[1])))
