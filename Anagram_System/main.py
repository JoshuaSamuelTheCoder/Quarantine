"""
# Two words are anagrams if they have the same letters in a different order, for example, 'stressed' and 'desserts', 'elbow' and 'below'.
#
# Design a system that manages anagrams.
# When queried for a word, the system should return all the words known by the system that are anagrams of the searched word, but not the word itself.
# Every time a word is searched, the system learns the word i.e., it adds it to the list of known words.
#
# Implement the function get_anagrams(word), which returns all the anagrams of the word (but not the word itself) and adds the word to the knowledge base if the word is being searched for the first time.

# Test cases (starting with an empty system).
# 1. System knows no words, therefore returns an empty list. 'trace' is added to the database.
# assert get_anagrams('trace') == []
# assert get_anagrams('trace') == []

# 2. 'trace' is already in the database, therefore the system returns it. 'cater' is added to the database.
# assert get_anagrams('cater') == ['trace'] "acert" -> "trace", "cater"

# 3. 'cater' and 'trace' are already in the database. The system returns 'cater'.
# assert get_anagrams('trace') == ['cater']

# 4. 'cater' and 'trace' are already in the database. The system returns ['cater', 'trace'] and adds 'react'.
# assert set(get_anagrams('react'))) == set(['cater', 'trace'])

# 5. 'cater', 'trace' and 'react' are already in the database. The system returns ['cater', 'trace', 'react'] and adds 'crate'.
# assert set(get_anagrams('crate'))) == set(['cater', 'trace', 'react'])

# 6. 'cater', 'trace', 'react' and 'crate' are already in the database. The system returns ['cater', 'trace', 'crate'].
# assert set(get_anagrams('react'))) == set(['cater', 'trace', 'crate'])

#Check if 2 words are anagrams -> HashMap Counter -> {'t':1, 'r':1...} , "cater" Costly
#Storing all the past words->

#Check if 2 words are anagrams, sort each word Hashmap: "sorted word" -> list of words
"""

class AnagramSystem(object):
    def __init__(self):
        self.freq = {}  #hashmap of keys: str, values: set()

    def get_anagram(self, st):
        new_s = str(sorted(st)) #key
        rtn_lst = set()

        if new_s in self.freq:
            lst = self.freq[new_s]

            rtn_lst = set(lst) #O(n)
            if st in rtn_lst:
                rtn_lst.remove(st)
            self.freq[new_s].add(st)
        else:
            self.freq[new_s] = set()
            self.freq[new_s].add(st)

        return rtn_lst

if __name__ == "__main__":

    system = AnagramSystem()

    print(system.get_anagram('trace') == set([]))
    print(system.get_anagram('trace') == set([]))
    print(system.get_anagram('cater') == set(["trace"]))
    print(system.get_anagram('react') == set(["trace", "cater"]))
    print(system.get_anagram('crate') == set(['cater', 'trace', 'react']))
    print(system.get_anagram('react') == set(['cater', 'trace', 'crate']))
