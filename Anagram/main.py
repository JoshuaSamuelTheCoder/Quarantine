"""
Problem:
Given some letters and a word, find out if that word can be formed using those letters
letters - b a c u s
word - abacus -> false
letters  - aaaaabbbbbccccc
word - abc -> true
word - pqr -> false

"""
#Time: O(len(letters) + len(word))
#Space: O(len(letters))

def wordCanBeFormed(letters, word):
    #letters: array of characters
    #word: string

    freq = {}
    for ch in letters:
        freq[ch] = freq.get(ch, 0) + 1

    for s in word:
        if s not in freq:
            return False
        freq[s] -= 1
        if freq[s] < 0:
            return False

    return True

if __name__ == "__main__":
    print(wordCanBeFormed(['b', 'a', 'c', 'u', 's'], "abc"))
    print(wordCanBeFormed(['a','a','a','a','a','b','b','b','b','b','c','c','c','c','c'], "abc"))
    print(wordCanBeFormed(['a','a','a','a','a','b','b','b','b','b','c','c','c','c','c'], "pqr"))
