

class Solution():

    def reverse(self, word):
        lst = []
        s = ""
        for i in range(len(word)):
            if word[i] == " ":
                lst.append(s)
                lst.append(" ")
                s = ""
            else:
                s += word[i]
        lst.append(s)



        lst = lst[::-1]
        st = "".join(lst[i] for i in range(len(lst)))
        return st





if __name__ == "__main__":

    sol = Solution()
    print(sol.reverse("I am being interviewed by Amazon"))
