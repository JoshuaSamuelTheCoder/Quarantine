"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(0, 1)
Output:
    3

Input:
solution.solution(19, 36)
Output:
    1
"""
BOARD_INC = 8
#takes 8 to move up/down a row
def isValid(old_pos, new_pos):

    #returns False if invalid move
    if new_pos < 0 or new_pos > BOARD_INC**2 - 1:
        #knock out invalid positions
        return False
    left_lst = [0,1]
    right_lst = [BOARD_INC-2,BOARD_INC-1]

    old_ind = old_pos % BOARD_INC
    new_ind = new_pos % BOARD_INC

    if (old_ind in left_lst and new_ind in right_lst) or (old_ind in right_lst and new_ind in left_lst):
        return False
    return True


def calculatePossibilities(val):
    #returns list of possible paths given a starting position
    inc = BOARD_INC
    up_left = val - 2*inc - 1
    up_right = val - 2*inc + 1
    down_left = val + 2*inc - 1
    down_right = val + 2*inc + 1

    right_up = val - inc + 2
    right_down = val + inc + 2
    left_up = val - inc - 2
    left_down = val + inc - 2

    poss = [up_left, up_right, down_left, down_right, right_up, right_down, left_up, left_down]
    return [ele for ele in poss if isValid(val, ele)]

def solution(src, dest):

    if src == dest:
        return 0

    #this problem's gonna be fun


    sol = float("inf")
    #to keep track of sol

    job_lst = []
    #load of paths need to take, queue structure

    seen = []
    #already seen squares

    job_lst.append((src,0))

    while len(job_lst) > 0:
        item, freq = job_lst.pop(0)

        if item not in seen:

            seen.append(item)

            #all 4 possibilities
            poss = calculatePossibilities(item)
            for i in poss:
                if i == dest:
                    sol = min(sol, freq+1)
                job_lst.append((i, freq+1))
    return sol



if __name__ == "__main__":


    print(solution(0, 1))
    #print(solution(19, 36))
