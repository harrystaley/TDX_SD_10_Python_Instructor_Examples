class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, val):
        # Compare the new value with the parent node
        if self.data:
            if val < self.data:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.data:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.data = val

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data, end=' ')
        if self.right:
            self.right.printtree()


if __name__ == "__main__":
    root = Node(100)
    root.insert(28)
    root.insert(33)
    root.insert(3)
    root.printtree()
