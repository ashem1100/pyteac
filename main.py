class Node:
    def __init__(self, label=None):
        self.label = label
        self.left_most_child = None
        self.right_sibling = None
        self.g_tree_address = None

    def left_most_child(self):
        return self.left_most_child

    def right_sibling(self):
        return self.right_sibling

    def label_node_val(self):
        return self.label

    def set_left_most_child(self, node):
        self.left_most_child = node

    def set_right_sibling(self, node):
        self.right_sibling = node

    def set_label_node(self, label):
        self.label = label

    def set_g_tree_address(self, g_tree):
        self.g_tree_address = g_tree

    def g_tree_address_val(self):
        return self.g_tree_address

    def print_label_node(self):
        print(f"{self.label}", end='')

    def preorder(self):
        self.print_label_node()
        child = self.left_most_child
        while child:
            child.preorder()
            child = child.right_sibling

    def postorder(self):
        child = self.left_most_child
        while child:
            child.postorder()
            child = child.right_sibling
        self.print_label_node()


class GTree:
    def __init__(self, label=None):
        self.root = Node(label)
        self.root.set_g_tree_address(self)

    def root_p(self):
        return self.root

    def create(self, n, g_tree_table, label):
        self.root.set_label_node(label)
        for i in range(n - 1, 0, -1):
            g_tree_table[i - 1].root_p().set_right_sibling(g_tree_table[i].root_p())
        self.root.set_left_most_child(g_tree_table[0].root_p())

    def preorder(self):
        print("PreOrder :")
        self.root_p().preorder()
        print("\n---------------------------------------")

    def postorder(self):
        print("PostOrder :")
        self.root_p().postorder()
        print("\n---------------------------------------")

    def parent(self, n, root):
        if n == root:
            print("No parent found")
            return None
        else:
            p = self.root_p()
            rs = self.root_p().left_most_child
            while rs:
                if rs != n.root_p():
                    temp = rs.g_tree_address_val().parent(n, root)
                    if temp:
                        return temp
                    else:
                        rs = rs.right_sibling
                else:
                    return p
        return None


def parenthood(a, root):
    print("\nParent ", end='')
    a.root_p().print_label_node()
    print(" = ", end='')
    root.parent(a, root).print_label_node()





if __name__ == "__main__":

    t21 = GTree('E')
    t22 = GTree('H')
    t23 = GTree('L')
    t2 = GTree()

    g_table1 = [t21, t22, t23]
    t2.create(3, g_table1, 'B')

    t1 = GTree('A')
    t3 = GTree('C')
    g_table2 = [t1, t2, t3]
    t4 = GTree()
    t4.create(3, g_table2, 'D')


    t4.preorder()
    t4.postorder()
    parenthood(t3, t4)
    parenthood(t2, t4)
    parenthood(t22, t4)
    parenthood(t21, t4)







