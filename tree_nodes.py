class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1 
            p=p.parent

        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level()
        print(spaces + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()
    
def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Microsoft"))
    laptop.add_child(TreeNode("Dell"))

    consoles = TreeNode("Consoles")
    consoles.add_child(TreeNode("PlayStation 5"))
    consoles.add_child(TreeNode("Nintendo Switch"))
    consoles.add_child(TreeNode("XBox"))

    root.add_child(laptop)
    root.add_child(consoles)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
