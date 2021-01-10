"""
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".



Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
Example 2:

Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
Example 3:

Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
"""

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        count = 0
        occurenceA = ""
        occurenceB = ""
        swappable = False
        seen = set()
        for i in range(len(A)):
            if A[i] != B[i]:
                if count == 0:
                    count += 1
                    occurenceA = A[i]
                    occurenceB = B[i]
                elif count == 1:
                    count += 1
                    if B[i] != occurenceA or A[i] != occurenceB:
                        return False
                else:
                    return False
            else:
                if A[i] in seen:
                    swappable = True
            seen.add(A[i])
        return (swappable and count == 0) or count == 2
