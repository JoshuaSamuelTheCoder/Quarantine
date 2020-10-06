"""
Two players are playing a game where white or black pieces are represented by a string, colors.
The game rules are as follows:

Wendy moves first and then they take alternate turns.
With each move, Wendy may remove a white piece that has adjacent white pieces on both sides.
Likewise, with each move, Bob may remove any black piece that has adjacent black pieces on both sides.
After a piece is removed, the string is reduced in size by one piece. For instance, removing "Y" from "XYZ" results in "XZ"
When a player can no longer move, they have lost the game.

Example:
colors = 'wwwbbbbbwww'

Wendy removes the piece w at index 1, colors = 'wwbbbbwww'
Bob removes the piece b at index 3, colors = 'wwbbbwww'
Wendy removes the piece w at index 6, colors = 'wwbbbww'
Bob removes the piece b from index 3, colors = 'wwbbww'
Wendy has no other move, so Bob wins. Return 'bob'

Determine who wins if Wendy and Bob both play with optimum skill. Return the string 'wendy' or 'bob'.

Input:
string colors: each colors[i] represents the color located at the index of i within the string.
Output:
string: the winner of the game, either 'wendy' or 'bob'

TestCase 1:
Input:
colors = wwwbb
Output:
'wendy'
Explanation:
There are five colors in the string. Wendy can remove any of the white pieces in the first move. After that the colors string
becomes 'wwbb'. Bob has no move since there is no black piece with exactly two black adjacent pieces, so Wendy wins.
"""

def gameWinner(colors):
    bobMoves = 0
    wendyMoves = 0
    move = 1
    for i in range(len(colors)):
        if colors[i] == "w":
            if move == 1:
                #increment Wendy
                countLetters += 1
            else:
                #done with Bob
                bobMoves += max(countLetters - 2, 0)
                countLetters = 1
                move = 1
        else:
            if move == 0:
                #increment Bob
                countLetters += 1
            else:
                #done with Wendy
                wendyMoves += max(countLetters - 2, 0)
                countLetters = 1
                move = 0
    if move == 0:
        bobMoves += max(countLetters - 2, 0)
    else:
        wendyMoves += max(countLetters - 2, 0)
    if wendyMoves > bobMoves:
        return 'wendy'
    else:
        return 'bob'
