from __future__ import division
import numpy as np
import fractions
from fractions import Fraction
from fractions import gcd
import math

def normalize(v):
    v_sum = np.sum(v)
    if v_sum == 0:
       return v
    return np.array(v / v_sum)

def split_matrix(m):
    #first 2 rows are usually nonzero
    transition_states = []
    feeding_states = []

    starting_index = 0
    for i in range(len(m)):
        if not np.any(m[i]):
            starting_index = i
            break

    if starting_index == 0:
        return None, None, None

    for i in range(len(m)):
        new_ind = np.asarray(normalize(m[i]), dtype=float)
        if i < starting_index:
            transition_states.append(new_ind[starting_index:])
            feeding_states.append(new_ind[:starting_index])

    return np.asarray(transition_states), np.asarray(feeding_states), False

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

def is_same(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


def get_lcm(arr):
    lcm = arr[0]
    for num in arr:
        lcm = lcm*num // gcd_recursive(lcm, num)
    return lcm

def get_fraction_lcm(arr):
    lcm = arr[0]
    for num in arr:
        lcm = int(lcm)*num // gcd_recursive(int(lcm), int(num))

    return lcm

def solution(m):
    # Your code here

    #Notes:
        #Markov Chain problem?
        #Steady state?
        #0, 1 nodes are transient, rest are recurrent

    transition_states, feeding_states, err = split_matrix(m)

    if err == None:
        return [1]*(len(m) + len(m[0]))

    f_const = np.eye(feeding_states.shape[0]) - feeding_states

    f_final = np.linalg.inv(f_const)

    limited = np.dot(f_final,transition_states).tolist()[0]

    converted = [Fraction(num).limit_denominator(max_denominator=10000000) for num in limited]

    denoms = [num.denominator for num in converted]
    lcm = int(get_lcm(denoms))


    un_normalized = [int(num*lcm) for num in converted] + [lcm]

    return un_normalized
