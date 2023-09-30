class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printll(self):
        node=self.head
        while node:
            print(str(node.data)+"-->",end=" ")
            node=node.next
        print("null")

    def printmid(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)

if __name__=="__main__":
    llist=linkedlist()
    for i in range(6,0,-1):
        llist.push(i)
        llist.printll()
        llist.printmid()