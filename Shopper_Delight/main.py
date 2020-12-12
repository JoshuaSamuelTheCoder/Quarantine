


def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    map = {}

    for j in priceOfJeans:
        for k in priceOfShoes:
            for s in priceOfSkirts:
                if j + k + s <= budgeted:
                    map[j+k+s] = map.get(j+k+s, 0) + 1

    sum_lst = list(map.keys())
    sum_lst.sort()
    count = 0
    for s in sum_lst:
        map[s] += count
        count += map[s]

    counter = 0
    for t in priceOfTops:
        target = budgeted - t
        counter += map[target]

    return counter

if __name__ == "__main__":
    t1 = [[2,3], [4], [2,3], [1,2], 10]

    print(getNumberOfOptions(*t1))
