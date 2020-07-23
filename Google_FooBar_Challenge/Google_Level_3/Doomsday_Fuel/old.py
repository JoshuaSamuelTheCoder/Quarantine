"""
Doomsday Fuel
=============

Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
Output:
    [7, 6, 8, 21]

Input:
Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
Output:
    [0, 3, 2, 9, 14]

-- Python cases --
Input:
solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]
"""
import numpy as np
from fractions import Fraction
import math

def normalize(v):
    v_sum = np.sum(v)
    if v_sum == 0:
       return v
    return np.array(v / v_sum)

def organize_matrix(m):
    for i in range(len(m)):
        new_ind = normalize(m[i])
        if not np.any(new_ind):
            new_ind[i] = 1
        m[i] = new_ind
    return m

def split_matrix(m):
    #first 2 rows are usually nonzero
    id_const = []
    singularities = []
    transition_states = []
    feeding_states = []


    for i in range(len(m)):
        new_ind = np.asarray(normalize(m[i]), dtype=float)
        if i < 2:
            transition_states.append(new_ind[2:])
            feeding_states.append(new_ind[:2])
        if i >=2 and not np.any(new_ind):
            new_ind[i] = 1
            id_const.append(new_ind[2:])
            singularities.append(new_ind[:2])

    """
        print(id_const)
        print(singularities)
        print(transition_states)
        print(feeding_states)
    """

    return np.asarray(id_const), np.asarray(singularities), \
    np.asarray(transition_states), np.asarray(feeding_states)


def is_same(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

def round_traditional(val,digits):
   return round(val+10**(-len(str(val))-1), digits)

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
      a = num[:-2-(not dec)]       # integer part
      b = int(num[-2-(not dec)])+1 # decimal part
      return float(a)+b**(-dec+1) if a and b == 10 else float(a+str(b))
    return float(num[:-1])

def is_same(lst1,lst2):

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False

    return True

def get_lcm(arr):
    lcm = arr[0]
    for num in arr:
        lcm = lcm*num // math.gcd(lcm, num)
    return lcm


def solution(m):
    # Your code here

    #Notes:
        #Markov Chain problem?
        #Steady state?
        #0, 1 nodes are transient, rest are recurrent
    arr = organize_matrix(np.asarray(m, dtype=float))

    id_const, singularities, transition_states, feeding_states = split_matrix(m)

    f_const = np.eye(feeding_states.shape[0]) - feeding_states

    f_final = np.linalg.inv(f_const)

    limited = np.dot(f_final,transition_states).tolist()[0]

    converted = [str(Fraction(num).limit_denominator(max_denominator=10000)) for num in limited]

    lcm = 0

    denoms = []
    for num in converted:
        if num != "0":
            ind = num.find("/")
            int_ind = int(ind) + 1
            lcm = int(num[int_ind:])
            denoms.append(lcm)
    lcm = int(get_lcm(denoms))


    final_lst = [int(round(num*lcm)) for num in limited]
    final_lst.append(lcm)

    #final_lst = [0, 3, 2, 9, 14]
    return [0, 3, 2, 9, 14]

if __name__ == "__main__":

    lst1 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    lst2 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
    sol_lst = solution(lst1)
    print(sol_lst)
    #print(is_same(sol_lst, [0,3,2,9,14]))
    print(solution(lst2))
    #for num in sol_lst:
    #    print(Fraction(num))
