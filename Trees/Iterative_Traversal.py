class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

def preOrder(root):
    pass

def postOrder(root):
    pass

def inOrder(root):
    current = root
    stack = []

    while True:
        # Reach the leftmost node of the current node
        if current is not None:
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            stack.append(current)
            current = current.left

        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done
        elif stack:
            current = stack.pop()
            print(current.value, end=" ")

            # We have visited the node and its left  
            # subtree. Now, it's right subtree's turn 
            current = current.right

        else:
            break
    print()

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    inOrder(root)



