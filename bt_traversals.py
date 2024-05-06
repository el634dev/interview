# All one liners

# Preorder traversal
def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []

# Inorder Traversal
def inorder(root):
  return inorder(root.left) + [root.val] + inorder(root.right) if root else []

# Postorder Traversal
def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []


# Using a class and separate functions
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

result = []

def in_order(root):
    if not root:
        return []

    in_order(root.left)
    result.append(root.val)
    in_order(root.right)
    return result

def pre_order(root):
    if not root:
        return []

    result.append(root.val)
    pre_order(root.left)
    pre_order(root.right)
    return result

def post_order(root):
    if not root:
        return []

    post_order(root.left)
    post_order(root.right)
    result.append(root.val)
    return result
