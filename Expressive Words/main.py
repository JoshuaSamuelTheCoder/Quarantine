"""
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy.



Example:
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        pointer_S = 0
        pointer_word = 0

        count = 0
        cache_letter = ""
        num_words = 0
        sticky = False
        encountered = 0

        for word in words:
            if len(word) > len(S):
                continue
            while(pointer_S < len(S)):
                if pointer_word < len(word) and word[pointer_word] == S[pointer_S]:
                    if count - encountered > 0 and sticky:
                        break
                    if cache_letter != word[pointer_word]:
                        cache_letter = word[pointer_word]
                        count = 2
                        encountered = 0
                        sticky = False
                    else:
                        encountered += 1
                    pointer_S += 1
                    pointer_word += 1
                else:
                    if cache_letter == S[pointer_S]:
                        pointer_S += 1
                        count -= 1
                        sticky = True
                    else:
                        if count > 0:
                            break
                        elif word[pointer_word] != S[pointer_S]:
                            count = 1
                            break
            if count - encountered <= 0 or (pointer_S == len(S) and pointer_word == len(word) and count == 2):
                num_words += 1
                #print(word)

            """
            if pointer_word in range(len(word)):
                print(word, count, ": im angry at " + str(pointer_word) + ", " + str(pointer_S))
            else:
                print(count - encountered, ": ", word)
                """
            pointer_word = 0
            pointer_S = 0
            encountered = 0
            sticky = False
            count = 0
            cache_letter = ""

        return num_words
