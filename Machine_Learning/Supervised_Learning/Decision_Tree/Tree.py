class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    

class Tree:
    def __init__(self):
        self.root = None

    def insert_Node(self, rootNode, value):
        if rootNode is None:
            self.root = Node(value)
        else:
            if value < rootNode.value:
                if rootNode.left is None:
                    rootNode.left = Node(value)
                else:
                    self.insert_Node(rootNode.left, value)
            else:
                if rootNode.right is None:
                    rootNode.right = Node(value)
                else:
                    self.insert_Node(rootNode.right, value)
    
    def inorder_traversal(self, rootNode):
        if rootNode:
            self.inorder_traversal(rootNode.left)
            print(rootNode.value, end=' ')
            self.inorder_traversal(rootNode.right)

# Example usage
if __name__ == '__main__':
    tree = Tree()

    tree.insert_Node(tree.root, 5)
    tree.insert_Node(tree.root, 3)
    tree.insert_Node(tree.root, 8)
    tree.insert_Node(tree.root, 2)
    tree.insert_Node(tree.root, 4)
    tree.insert_Node(tree.root, 7)
    tree.insert_Node(tree.root, 9)

    tree.inorder_traversal(tree.root)