from __future__ import division
import compare

def add(i):
    return i+1

def sub(i):
    return i-1

def div(i):
    return int(i / 2)

def divides(i,j):
    #returns True if i divides j
    return i % j == 0

def old_solution(n):
    # Your code here
    #Notes
        #make it a multiple of 2 then divide

    num = int(n)
    num_lst = []
    counter = 0
    while num != 1:
        num_lst.append(num)
        if num % 2 == 0:
            num = div(num)
        else:
            #move to the closest multiple of 2
            closest = float("inf")
            minDist = float("inf")
            e = 0
            while True:
                m = 2**e
                dist = abs(num-m)
                if dist < minDist:
                    minDist = dist
                    closest = m
                elif dist >= minDist:
                    #finished
                    break
                e += 1
            if closest <= num:
                num = sub(num)
            else:
                num = add(num)
        counter += 1

    num_lst.append(1)
    return num_lst

def solution(n):
    # Your code here
    #Notes
        #make it a multiple of 2 then divide

    num = int(n)
    num_lst = []
    counter = 0
    while num != 1:
        num_lst.append(num)
        if num % 2 == 0:
            num = div(num)
        else:
            #move to the closest multiple of 2
            closest = float("inf")
            minDist = float("inf")
            e = 0
            while True:
                m = 2**e
                dist = abs(num-m)
                if dist < minDist:
                    minDist = dist
                    closest = m
                elif dist >= minDist:
                    #finished
                    break
                e += 1
            if closest <= num or minDist > 9:
                num = sub(num)
            else:
                num = add(num)
        counter += 1

    num_lst.append(1)
    return num_lst

def new_solution(n):
    # Your code here
    #Notes
        #make it a multiple of 2 then divide

    num = int(n)
    num_lst = []
    counter = 0
    while num != 1:

        num_lst.append(num)
        if num % 2 == 0:
            num = div(num)
        else:
            #move to whichever number can divide the biggest multiple of 2
            num_above = num + 1
            num_below = num - 1
            e = 0
            new_num = 0
            m = 0
            while True:
                m = 2**e
                if divides(num_above, m) and divides(num_below, m):
                    pass
                elif divides(num_above, m) and not divides(num_below, m):
                    new_num = num_above
                    break
                else:
                    new_num = num_below
                    break
                e += 1

            if num_below == 2**(e-1):
                new_num = num_below
            if new_num > num:
                num = add(num)
            else:
                num = sub(num)


        counter += 1

    num_lst.append(1)
    return num_lst

def print_lst(lst):
    for n in lst[:-1]:
        print(str(n) + "->", end="", flush=True)
    print(1)

if __name__ == "__main__":
    counter = 0
    """
    for i in range(1,1000):
        old = old_solution(i)
        new = solution(i)
        if len(old) < len(new):
            print("Old is better than new for " + str(i))
            print_lst(old)
            print_lst(new)
            counter += 1
    print("Old is better than new " + str(counter) + " times")
    """

    lst = []
    for i in range(1,100):
        old = compare.answer(i)
        new = new_solution(i)
        if len(old) < len(new):
            print("Old is better than new for " + str(i))
            print_lst(old)
            print_lst(new)
            counter += 1
        elif len(new) > len(old):
            print("hmmm")
        else:
            print_lst(old)
            #print_lst(new)
    print("Old is better than new " + str(counter) + " times")

    #print_lst(new_solution(3))


    #solution(3)
    #15->16->8->4->2->1
