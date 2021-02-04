"""
Given an array of first and last names, output the initials such as any repeats are appended with a
number as followed.

Input: array ["joshua samuel",  russell peters, sam g, "jack smith", rachel pasta]
Output: array ["js, "rp", "sg", "js1", "rp1"]
"""

def parseArray(array):

    freq = {}
    rtn_lst = []

    for a in array:
        lst = list(a.split(" "))
        st = lst[0][0] + lst[1][0]
        if st in freq:
            rtn_lst.append(st + str(freq[st]))
            freq[st] = freq[st] + 1
        else:
            rtn_lst.append(st)
            freq[st] = 1
    return rtn_lst

input_lst = ["joshua samuel",  "russell peters", "sam g",
 "jack smith", "rachel pasta"]
print(parseArray(input_lst))
