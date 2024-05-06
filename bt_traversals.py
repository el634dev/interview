# All one liners below
# ----------------------
# Preorder traversal
def preorder(root):
  """
  Time Complexity: O(1) -> Constant
  """
  return [root.val] + preorder(root.left) + preorder(root.right) if root else [] # O(1)

# ----------------------
# Inorder Traversal
def inorder(root):
  """
  Time Complexity: O(1) -> Constant
  """
  return inorder(root.left) + [root.val] + inorder(root.right) if root else [] # O(1)

# ----------------------
# Postorder Traversal
def postorder(root):
  """
  Time Complexity: O(1) -> Constant
  """
  return postorder(root.left) + postorder(root.right) + [root.val] if root else [] # O(1)

# ----------------------
# Using a class and separate functions
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

result = []

# ----------------------
# In order traversal
def in_order(root):
  """
  Time Complexity: O(1) -> Constant
  """
  if not root: # O(1)
      return [] # O(1) 

  in_order(root.left) # O(1)
  result.append(root.val) # O(1)
  in_order(root.right) # O(1)
  return result # O(1)

# ----------------------
# Pre order traversal
def pre_order(root):
   """
    Time Complexity: O(1) -> Constant
   """
  if not root:  # O(1)
      return []  # O(1)

  result.append(root.val) # O(1)
  pre_order(root.left) # O(1)
  pre_order(root.right) # O(1)
  return result # O(1)

# ----------------------
# Post order traversal
def post_order(root):
   """
    Time Complexity: O(1) -> Constant
   """
  if not root: # O(1)
      return [] # O(1)

  post_order(root.left) # O(1)
  post_order(root.right) # O(1)
  result.append(root.val) # O(1)
  return result # O(1)
