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
        #dynamic programming
        #need to add wall feature
        #need to add 1 time wall break feature
    #Questions:
        #does removing a wall count as a move? probably not hmmm

    job_lst = []

    sol = float("inf")

    global GRID_HEIGHT
    global GRID_WIDTH
    global GRID

    GRID_HEIGHT = len(map)
    GRID_WIDTH = len(map[GRID_HEIGHT-1])
    GRID = map

    job_lst.append(((0,0), 1, True, []))

    while len(job_lst) > 0:
        loc, freq, hasTrumpCard, seen_lst = job_lst.pop(0)

        if loc not in seen_lst:

            seen_lst.append(loc)
            poss = calculatePossibilities(loc, hasTrumpCard)
            for p in poss:
                new_loc, tc = p
                x,y = new_loc
                if x == GRID_WIDTH - 1 and y == GRID_HEIGHT - 1:
                    sol = min(sol, freq + 1)
                else:
                    copy_lst = seen_lst[:]
                    job_lst.append((new_loc, freq+1, tc, copy_lst))

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
