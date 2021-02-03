#Python is the worst language for decimals
import numpy as np
from decimal import Decimal, getcontext
class Solution(object):
    def calculateHelper(self, r, new_sol):

        if float(r) == 0:
            #print("hm")
            self.sol_array.append(new_sol)
            return
        elif r < 0:
            #print("wrong")
            return

        for k,v in self.menu.items():
            new_sol[k] = new_sol.get(k, 0) + 1

            val = float(r - v)
            self.calculateHelper(val, new_sol)

            new_sol = {}


    def calculate(self, menu, receipts):
        getcontext().prec = 2
        #start algorithm
        self.sol_array = []

        self.menu = menu
        self.reciepts = receipts

        #pseudocode
        for r in receipts:
            #helper
            print(r)
            print(self.sol_array)
            new_sol = {}
            self.calculateHelper(r, new_sol)
        return self.sol_array

if __name__ == "__main__":

    menu = {}
    menu["veggie sandwich"] = 6.85
    menu["extra veggies"] = 2.20
    menu["chicken sandwich"] = 7.85
    menu["extra chicken"] = 3.20
    menu["cheese"] = 1.25
    menu["chips"] = 1.40
    menu["nachos"] = 3.45
    menu["soda"] = 2.05

    reciepts = [4.85, 11.05, 13.75, 17.75, 18.25, 19.40, 28.25, 40.30, 75.00]
    sol = Solution()

    print(sol.calculate(menu, reciepts))
