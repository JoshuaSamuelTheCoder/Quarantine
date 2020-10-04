"""
A quality agent is responsible for inspecting samples of the finished products in the production line.
Each sample contains defective and non-defective products represented by 1 and 0 respectively.
After placing the product samples sequentially in a two-dimensional square matrix of product samples,
determine the size of the largest square area of defective products.

Example:
n x n = 5 x 5 matrix of product samples
samples = [[1,1,1,1,1], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,1,1]]

-----------
|1 1 1 1 1|
|1 1 1 0 0|
|1 1 1 0 0|
|1 1 1 0 0|
|1 1 1 1 1|
-----------
Explanation:
The first square area of defective products is a sub-matrix 3x3 starting at (0,0) and ending at (3,3)
The second square area of defective products is also a sub-matrix 3x3 starting at (1,0) and ending at (4,3)
The third square area of defective products is also a sub-matrix 3x3 starting at (2,0) and ending at (5,3)
The size of the largest square area of defective products is 3.

Function Description:
Input:
    int samples[n][n]: a two-dimensional array of integers
Returns:
    int: an integer that represents the size of the largest square sub-matrix of defective products
Note: 1 denotes defective products, 0 denotes non-defective products
                                        -------
Sample Testcase 0:                      |1 1 1|
samples[] size = 3                      |1 1 0|
samples[i][] size = 3                   |1 0 1|
samples = [[1,1,1],[1,1,0],[1,0,1]]     -------

Explanation:
The first square area of defective products is a sub-matrix 2x2 starting at (0,0) and ending at (1,1)
The other square area of defective products are a sub-matrix 1x1 at (2,0), (0,2), (2,2)
The size of the largest square area of defective products is 2.
                                        -------
Sample Testcase 1:                      |0 1 1|
samples[] size = 3                      |1 1 0|
samples[i][] size = 3                   |1 0 1|
samples = [[0,1,1],[1,1,0],[1,0,1]]     -------

Explanation:
All square area of defective products are a sub-matrix 1x1 at (0,1), (0,2), (1,1), (2,0) and (2,2)
The size of the largest square area of defective products is 1.
"""

def fillArray(samples, dp):
    mx = 0
    for i in range(len(samples)):
        for j in range(len(samples)):
            if samples[i][j] == 1:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + 1)
                mx = max(mx, dp[i][j])
            else:
                dp[i][j] = 0
    return mx
def largestArea(samples):
    dp = [[0 for i in range(len(samples))] for j in range(len(samples[0]))]
    return fillArray(samples, dp)
