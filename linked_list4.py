from http.client import NETWORK_AUTHENTICATION_REQUIRED


class DoubleNode:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,value):
        new_mode=DoubleNode(value)

        if self.hand is None:
            self.head=new_node
            self.tail=new_node
            print("Head Node Created",self.head.value)
            return

        new.node.prev=self.tail
        self.tail.next=new.node
        self.tail=new_node
        print("Appended new Model with value",self.tail.value)

dllist = DoublyLinkedList()
dllist.append("First Node")
