"""
Binary Tree Inorder Traversal - Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

"""
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

"""

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?

# ----------------
# SOLUTIONS
from typing import Optional, List


class TreeNode:
    """Binary Tree Class"""
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class RecursiveSolution:
    """Recursive Solution"""
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []
        def dfs(current_node, res):

            if not current_node:
                return

            dfs(current_node.left, res)
            res.append(current_node.val)
            dfs(current_node.right, res)

        dfs(root, res)
        return res

# ------------------
# Iterative Solution
class Iterative:
    """Iterative Solution"""
    def inorder_traversal_2(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res, stack = [], []
        currentNode = root
        while stack or currentNode:

            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            
            currentNode = stack.pop()
            res.append(currentNode.val)
            currentNode = currentNode.right
        return res

"""
Why O(N) time and space?

Time Complexity:
The code visits each node of the binary tree once and performs constant-time operations within each iteration of the while loop. 
Therefore, the time complexity is O(N), where N is the number of nodes in the binary tree.

Space Complexity:
The space complexity depends on the maximum number of nodes in the stack at any point during the traversal. In the worst case, 
the stack can contain all nodes of the tree for a skewed tree.
Therefore, the space complexity is O(N), where N is the number of nodes in the binary tree.
"""

"""
How does this all work?

Initialization:
It initializes an empty list res to store the inorder traversal result.
It initializes an empty stack stack to assist in the traversal.
It initializes a variable currentNode to the root of the binary tree.

Inorder Traversal:
It enters a while loop that continues until either the stack is empty and currentNode is None.
Within each iteration:
It traverses the left subtree of the current node and pushes all nodes encountered onto the stack until reaching the leftmost leaf node (currentNode becomes None).
It pops the top node currentNode from the stack, appends its value to the result list res, and moves to its right child.

Return:
After traversing all nodes of the binary tree in inorder fashion, it returns the result list res.
"""
