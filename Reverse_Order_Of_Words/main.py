"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Example 4:
Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Example 5:
Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
"""

def reverseWords(s):
    rtn_lst = []
    output_s = ""

    curr_word = ""
    for ch in s:
        if ch != " ":
            curr_word += ch
        elif ch == " " and curr_word != "":
            rtn_lst.append(curr_word)
            curr_word = ""

    if curr_word != "":
        rtn_lst.append(curr_word)

    length = len(rtn_lst)
    for i,word in enumerate(rtn_lst):
        if i == length - 1:
            output_s += rtn_lst[length - i - 1]
        else:
            output_s += rtn_lst[length - i - 1] + " "

    return output_s

if __name__ == "__main__":
    print(reverseWords("  Bob    Loves  Alice   "))
    print(reverseWords("Alice does not even like bob"))
    print(reverseWords("a good   example"))
    print(reverseWords("  hello world  "))
