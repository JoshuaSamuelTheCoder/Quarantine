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
