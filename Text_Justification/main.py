"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

class Solution(object):

    def frontload(self, c_list, r_list, leeway):
        #rint(leeway)
        numWords = max(len(c_list) - 1, 1)

        space = 0
        if len(c_list) == 1:
            space = self.maxWidth - len(c_list[0])

        div, rem = leeway // numWords, leeway % numWords

        st = ''

        i = 0
        while i < len(c_list) - 1:
            word = c_list[i]
            st += word + " "*div
            if rem > 0:
                st += " "
                rem -= 1

            i += 1

        st += c_list[-1] + " "*space
        r_list.append(st)

    def lastload(self, c_list, r_list, leeway):

        st = ''
        i = 0
        while i < len(c_list) - 1:
            st += c_list[i] + ' '
            i += 1

        st += c_list[-1]
        st += " "*(leeway-len(c_list) + 1)
        r_list.append(st)


    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        self.maxWidth = maxWidth
        st = ''
        cache_lst = []
        rtn_lst = []
        i = 0
        while(True):
            if i == len(words):
                #frontload last line
                self.lastload(cache_lst, rtn_lst, self.maxWidth-len(st) + len(cache_lst))
                break

            word = words[i]

            if len(st) + len(word) > self.maxWidth:
                #frontload st
                self.frontload(cache_lst, rtn_lst, self.maxWidth-len(st) + len(cache_lst))

                i -= 1
                st = ''
                cache_lst = []
            else:
                st += word + " "
                cache_lst.append(word)
            i += 1

        return rtn_lst
