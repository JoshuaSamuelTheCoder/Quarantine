/*
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
*/

void setZeroes(int** matrix, int matrixSize, int* matrixColSize){

    int column0 = 1;
    int row0 = 1;


    for(int i = 0; i < matrixSize; i++) {
        for(int j = 0; j < matrixColSize[i]; j++) {
            if (matrix[i][j] == 0) {
                if(i == 0 && j == 0) {
                    row0 = 0;
                    column0 = 0;
                } else if(i == 0) {
                    row0 = 0;
                } else if(j == 0) {
                    column0 = 0;
                } else {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
    }

    for(int j = 1; j < matrixColSize[0]; j++) {
        if (matrix[0][j] == 0) {
            for(int k = 1; k < matrixSize; k++) {
                matrix[k][j] = 0;
            }
        }
    }

    for(int i = 1; i < matrixSize; i++) {
        if (matrix[i][0] == 0) {
            for(int k = 0; k < matrixColSize[i]; k++) {
                matrix[i][k]  = 0;
            }
        }
    }

    if (row0 == 0) {
        for(int k = 0; k < matrixColSize[0]; k++) {
                matrix[0][k] = 0;
        }
    }
    if (column0 == 0) {
        for(int k = 0; k < matrixSize; k++) {
                matrix[k][0] = 0;
        }
    }
}
