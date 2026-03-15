class BTreeNode:
    def __init__(self):
        self.keys = []
        self.pointers = []
        self.left_sibling = None
        self.right_sibling = None
