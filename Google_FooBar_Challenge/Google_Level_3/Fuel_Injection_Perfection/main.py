from __future__ import division

def add(i):
    return i+1

def sub(i):
    return i-1

def div(i):
    return i >> 1

def solution(n):
    # Your code here
    #Notes
        #make it a multiple of 2 then divide

    num = int(n)

    counter = 0
    while num != 1:
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
                if dist > minDist:
                    minDist = dist
                    closest = m
                elif dist < minDist:
                    #finished
                    break
                e += 1
            if closest > num:
                num = add(num)
            else:
                num = sub(num)
        counter += 1
    return counter
if __name__ == "__main__":

    a = 124480579411363943422977485485450829978158403576349485507396127987323092328068524587695005561434534623452345436346456353425362283769712245781118297614280332424240701048410620648401132628401374562794562558123463462235342526466804149296501029546541499918765438784295157088047123009825235235168758962399

    print ("*********")
    print (answer(4))
    print ("*********")
    print (answer(15))
    print ("*********")
    print (answer(768))
    print ("^^^^^^^^^^^^^^")
    print (answer(1235))
    print ("**********")
    print (answer(65535))
    print ("=============")
    print (answer(947712))
    print ("*********")
    print (answer(17542149120))
    print ("*********")
    print (answer(15755622182313818849280))
    print ("*********")
    print (answer(a))
