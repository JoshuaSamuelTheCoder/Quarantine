"""
Given two arrays of strings, determine whether corresponding elements contain a common substring

Example:
a = ["ab","cd","ef"]
b = ["af","ee","ef"]

Make the following decisions:
i a[i] b[i] Common Result
0 ab   af   a      YES
1 cd   ee          NO
2 ef   ef   ef     YES

For each test, print the result on a new line, either YES if there is a common string, or NO

Function Description:
Complete the function commonSubstring in the editor below. For each a[i], b[i] pair, the function
must print YES if they share a common substring, or NO on a new line

Input:
    string a[n]: an array of strings
    string b[n]: an array of strings
Returns:
    void: Output should be printed to stdout rather than returned

Sample Testcase 1:
a[] size n = 2
a = ["hello", "hi"]
b[] size n = 2
b = ["world", "bye"]
Sample Output:
YES
NO

Explanation:
i a[i]   b[i]   Common  Output
0 hello  world  o,l     YES
1 hi     bye            NO
"""

def commonSubstring(a, b):
    freq = set()
    for i in range(len(a)):
        for j in range(len(a[i]):
            freq.add(a[i][j])
        for k in range(len(b[i])):
            if b[i][k] in freq:
                print("YES")
                break
        freq = set()
        if k == len(b[i]) - 1:
            print("NO")
