"""
Different compression techniques are used in order to reduce the size of the messages sent over the web.
An algorithm is designed to compress a given string by describing the total number of consecutive occurences
of each charcter next to it. For examples, consider the string "abaasass". Group the consecutive occurence of each character.

If a character only occurs once, it is added to the compressed string. If it occurs consecutive times, the character is added
to the string followed by an integer representing the number of consecutive occurences. Thus the compressed form of the string is "aba2sas2".

Function Description:
Input:
    string message: a string
Returns:
    string: the compressed message

Sample TestCase 1:
message = "abaabbbc"
Sample Ouput:
"aba2b3c"

Explanation:
Group the consecutive occurrences of each character to get "{a}{b}{aa}{bbb}{c}" in compressed form: "aba2b3c".
"""

def compressedString(message):
    rtn_st = ""
    freq_letter = ""
    freq = 0
    for i,s in enumerate(message):
        if s != freq_letter and freq_letter == "":
            rtn_st += s
            freq_letter = s
            freq = 1
        elif s != freq_letter and freq == 1:
            freq = 1
            rtn_st += s
            freq_letter = s
        elif s != freq_letter and freq > 1:
            rtn_st += str(freq)
            freq = 1
            rtn_st += s
            freq_letter = s
        else:
            freq += 1
    if freq > 1:
        rtn_st += str(freq)
    return rtn_st 
