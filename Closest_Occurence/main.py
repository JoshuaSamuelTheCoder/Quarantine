
#https://leetcode.com/discuss/interview-question/402031/IBM-or-OA-2019-or-Who's-the-closest

def closestOccurence(st, queries):

    freq = {}
    closest = []
    for i,s in enumerate(st):
        freq[s] = freq.get(s, []) + [i]

    for q in queries:
        mn = float("inf")
        for v in freq[st[q]]:
            if v != q:
                if q - v < mn:
                    mn = v
        mn = -1 if mn == float("inf") else mn
        closest.append(mn)
    return closest




if __name__ == "__main__":

    testCase1 = ["hackerrank", [4,1,6,8]]
    testCase2 = ["aaaa", [0,1,2,3]]
    testCase3 = ["sam", [1]]
    testCases = [testCase1, testCase2, testCase3]

    for i,t in enumerate(testCases):
        print("TestCase", i, "is", closestOccurence(t[0], t[1]))
