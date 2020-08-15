#This was my first solution that I got pretty quickly
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        #figure out if it's possible
        #make the swaps and return the minimum

        poss = []

        poss.append(A[0])
        if A[0] != B[0]:
            poss.append(B[0])

        counter = 0
        i = 0
        while i < len(A): #assumption that len(A) == len(B)
            if len(poss) == 1:
                #only 1 possibility
                if poss[0] != A[i] and poss[0] != B[i]:
                    return -1
            else:
                for num in poss:
                    if num != A[i] and num != B[i]:
                        poss.remove(num)
            i += 1

        #poss[0] is our target
        i = 0
        counterA = 0
        counterB = 0
        while i < len(A):
            if poss[0] != A[i]:
                counterA += 1
            if poss[0] != B[i]:
                counterB += 1
            i += 1


        return min(counterA, counterB)
