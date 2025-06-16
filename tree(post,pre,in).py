class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(5)

    print("inorder traversal:", end=" ")
    inorder(root)
    print()

    print("preorder traversal:", end=" ")
    preorder(root)
    print()

    print("postorder traversal:", end=" ")
    postorder(root)
    print()
