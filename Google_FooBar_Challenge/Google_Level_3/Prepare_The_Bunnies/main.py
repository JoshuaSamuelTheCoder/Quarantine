"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions.

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1).

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Test cases
==========

Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7

Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11
"""

def isValid(x,y):
    #checks if a location is valid in the grid

    #outside grid
    if x >= 0 and x < GRID_WIDTH and y >= 0 and y < GRID_HEIGHT:
        return True

    return False

def isWall(x,y):
    #is a wall

    if GRID[y][x] == 1:
        return True
    return False

def calculatePossibilities(location, hasTrumpCard):
    #returns a list of neighbors given location
    x,y = location

    poss = []

    for i,j in [(x, y+1), (x, y-1), (x+1, y),(x-1, y)]:

        #valid and not used TC
        #not valid and not used TC  <-- i don't want this possibility
        #not valid and used TC
        if isValid(i,j):
            if not isWall(i,j):
                poss.append(((i,j), hasTrumpCard))
            elif hasTrumpCard:
                poss.append(((i,j), False))

    return poss

def solution(map):
    # Notes:
        #bfs with a twist

    job_lst = []

    seen = []
    seen_after_tc = []

    sol = float("inf")

    global GRID_HEIGHT
    global GRID_WIDTH
    global GRID

    GRID_HEIGHT = len(map)
    GRID_WIDTH = len(map[GRID_HEIGHT-1])
    GRID = map

    job_lst.append(((0,0), 1, True))

    while len(job_lst) > 0:
        loc, freq, hasTrumpCard = job_lst.pop(0)

        s = []
        if hasTrumpCard:
            s = seen
        else:
            s = seen_after_tc

        if loc not in s:

            s.append(loc)
            poss = calculatePossibilities(loc, hasTrumpCard)
            for p in poss:
                new_loc, tc = p
                x,y = new_loc
                if x == GRID_WIDTH - 1 and y == GRID_HEIGHT - 1:
                    sol = min(sol, freq + 1)
                else:
                    job_lst.append((new_loc, freq+1, tc))

    return sol


if __name__ == "__main__":


    maze1 = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] #Answer 21
    maze2 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] #Answer 7
    maze3 = [[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]] #Answer 7
    maze4 = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] #Answer 7
    maze5 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] #Answer 11

    print(solution(maze1))
    print(solution(maze2))
    print(solution(maze3))
    print(solution(maze4))
    print(solution(maze5))



    #print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
