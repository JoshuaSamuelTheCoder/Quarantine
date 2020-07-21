def solution(l, t):
    # Your code here

    l_ind_val = 0
    r_ind_val = 0
    sum_val = 0
    found = False
    counter = 0
    i = 0
    while counter < len(l) and i < len(l):
        val = l[i]
        sum_val += val
        if sum_val == t:
            found = True
            r_ind_val = i
            break
        elif sum_val > t:
            i = counter
            counter += 1
            l_ind_val = counter
            sum_val = 0
        i += 1


    return [l_ind_val, r_ind_val] if found else [-1, -1]


if __name__ == "__main__":


    print(solution([1, 2, 3, 4], 15))
    print(solution([4, 3, 10, 2, 8], 12))

    print(solution([4, 3, 5, 7, 8],12))
