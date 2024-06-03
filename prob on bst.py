class bst:
    def __init__(self,key):
        self.key=key
        self.l_child=None
        self.r_child=None

    def insert_node(self,data):
        if self.key is None:
            return
        if self.key==data:
            return
        if self.key>data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=bst(data)
        else:
            if self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=bst(data)

root=bst(40)
root.insert_node(30)
root.insert_node(50)
root.insert_node(6)
print(root.key)
print(root.l_child.key)
print(root.r_child.key)
