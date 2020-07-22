def solution(lst):


    outcomes = {}

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] % lst[i] == 0:
                if lst[j] not in outcomes.get(lst[i], []):
                    outcomes[lst[i]] = outcomes.get(lst[i], []) + [lst[j]]

    num_solutions = 0
    for k in outcomes.keys():
        first_outcomes = outcomes[k]
        for f in first_outcomes:
            second_outcomes = outcomes.get(f, [])
            num_solutions += len(second_outcomes)

    return num_solutions


if __name__ == "__main__":

    #Notes
    #i < j < k



    print(solution([1, 1, 1]))
