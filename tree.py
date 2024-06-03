class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class tree:
    def __init__(self):
        self.root=None





tr=tree()

node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)
node5=node(50)
node6=node(60)
node7=node(70)
        

tr.root=node1
node1.next=node2
node1.prev=node3

node2.next=node4
node2.prev=node5

node3.next=node6
node3.prev=node7



