"""
Maximum Depth of Binary Tree - Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.
"""

"""
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3
"""

"""
Example 2:

Input: root = [1,null,2]
Output: 2
"""

# --------------
# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# --------------
# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --------------
# Solutions
# --------------

# Recursion
class Recursion:
    def maxDepth(self, root):
        """
        Time Complexity: O(1) -> Constant
        Space Complexity: O(1) -> Constant
        """
        # Base Case if there is no root
        if not root: # O(1)
            return 0 # O(1)

        # Get the left depth
        l_depth = self.maxDepth(root.left) # O(1)
        # Get the right depth
        r_depth = self.maxDepth(root.right) # O(1)
        # Return the max number from both sides plus 1
        return max(l_depth,r_depth) + 1 # O(1)

# --------------
# One Liner
class One:
    def max_depth_2(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(1) -> Constant
        Space Complexity: O(1) -> Constant
        """
        return 0 if not root else max(self.max_depth_2(root.left), self.max_depth_2(root.right)) + 1


# --------------
# Iterative
class Iterative:
    def max_depth_3(self, root: TreeNode) -> int:
        """
        Time Complexity: O(n) -> Linear Time
        Space Complexity: O(n) -> Linear Time
        """
        # Base Case if there is no root
        if not root: # O(1)
            return 0 # O(1)

        # Add root in the front
        tree = deque([root]) # O(1)
        # Initlize num_node_level to 1
        num_node_level = 1 # O(1)
        # Initlize levels to 0
        levels = 0 # O(1)

        while tree: # O(n)
            node = tree.popleft() # O(1)
            if node.left: # O(1)
                tree.append(node.left) # O(1)
            if node.right: # O(1)
                tree.append(node.right) # O(1)
            num_node_level -= 1 # O(1)
            if num_node_level == 0: # O(1)
                levels += 1 # O(1)
                num_node_level = len(tree) # O(1)

        return levels # O(1)
