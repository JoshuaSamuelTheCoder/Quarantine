class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        pointer_S = 0
        pointer_word = 0

        num_words = 0

        for word in words:
            if len(word) > len(S):
                continue
            cache_S = S
            cache_word = word
            cache_letter = ""
            num_encountered = 0
            while cache_S != "":

                if(cache_letter == ""):
                    parse_S = cache_S[0:1]
                    parse_word = cache_word[0:1]

                    if cache_word == "":
                        cache_word = "no"
                        break

                    if(parse_word == parse_S):
                            cache_letter = parse_S
                    else:
                        break
                    cache_S = cache_S[1:]
                    cache_word = cache_word[1:]
                else:

                    parse_S = cache_S[0:1]

                    if(parse_S != cache_letter):
                        cache_letter = ""
                        num_encountered = 0
                    else:
                        num_encountered += 1
                        cache_S = cache_S[1:]
                    if num_encountered == 2:
                            if cache_word[0:1] and cache_word[0:1] == cache_letter:
                                cache_letter = ""


            if cache_word == "" and (num_encountered > 1 or num_encountered == 0):
                num_words += 1
                print(word)



        return num_words
