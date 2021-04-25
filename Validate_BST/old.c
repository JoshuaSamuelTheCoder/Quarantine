/*
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
*/

#include <limits.h>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define MIN(A,B) ((A) < (B) ? (A):(B))
#define MAX(A,B) ((A) > (B) ? (A):(B))

bool isValidBSTChild(struct TreeNode *root, int direction, long int parent_left_val, long int parent_right_val) {

    if (root == NULL || (root->left == NULL && root->right == NULL)) {
        return true;
    }
    bool answer = true;

    bool left = true;
    if (root->left != NULL) {
        bool check_parent = false;
        long value_left = 0, value_right = 0;
        value_left = MIN(parent_left_val, root->val);
        value_right = MIN(root->val, parent_right_val);
        if (direction) {
            check_parent = (root->left->val < parent_right_val) && (root->left->val > parent_left_val);
        } else {
            check_parent = (root->left->val > parent_left_val) && (root->left->val > parent_left_val);
        }
        if (root->left->val < root->val && check_parent) {
            left = isValidBSTChild(root->left, 1, value_left, value_right);
        } else {
            return false;
        }
        answer = answer && left;
    }

    bool right = true;
    if (root->right != NULL) {
        bool check_parent = false;
        long value_left = 0, value_right = 0;
        value_left = MAX(parent_left_val, root->val);
        value_right = MAX(root->val, parent_right_val);
        if (direction) {
            check_parent = (root->right->val < parent_right_val) && (root->right->val < parent_right_val);
        } else {
            check_parent = (root->right->val > parent_left_val) && (root->right->val < parent_right_val);
        }

        if (root->right->val > root->val && check_parent) {
            right = isValidBSTChild(root->right, 0, value_left, value_right);
        } else {
            return false;
        }
        answer = answer && right;
    }
    return answer;
}

bool isValidBST(struct TreeNode* root){


    if (root == NULL || (root->left == NULL && root->right == NULL)) {
        return true;
    }
    bool answer = true;

    bool left = true;
    if (root->left != NULL) {
        if (root->left->val < root->val) {
            left = isValidBSTChild(root->left, 1, LONG_MIN, root->val);
        } else {
            return false;
        }
        answer = answer && left;
    }

    bool right = true;
    if (root->right != NULL) {
        if (root->right->val > root->val) {
            right = isValidBSTChild(root->right, 0, root->val, LONG_MAX);
        } else {
            return false;
        }
        answer = answer && right;
    }
    return answer;

}
