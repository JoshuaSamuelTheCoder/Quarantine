def numHouses(caseNum, costs, amount):

    costs.sort()

    cpy = amount
    i = 0
    while cpy > 0 and i < len(costs):
        cpy -= costs[i]
        i += 1

    if cpy < 0:
        i -= 1

    print("Case #" + caseNum + ": ", i)


if __name__ == "__main__":

    numTestCases = input()

    for i in range(int(numTestCases)):

        n, m, b = input().split()

        beauty_lst = []
        for j in range(n):
            beauty_lst.append(list(map(int, input().split())))

        numHouses(str(i+1), beauty_lst, int(b))
