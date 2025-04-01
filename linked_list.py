class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node




class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_LL(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} => "
            node = node.next_node

        ll_string += "None"
        print(ll_string)



    # def ins_0(self,data):
    #     node = Node("data",self.head)
    #     #still deliberately assign class var
    #     self.head = node
    # def ins_N(self,data):
    #     node = Node("data",self.last_node)


ll = LinkedList()

node2 = Node("2",None)
node1 = Node("fir",node2)

ll.head = node1
ll.print_LL()



# LinkedList.head = node1
# LinkedList.last_node = node2 # ?
