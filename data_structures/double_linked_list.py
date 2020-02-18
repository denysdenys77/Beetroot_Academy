# Реализовать добавление в начало, добавление в конец и добавление после определенного элемента в двусвязном списке.


class Node:

    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def add_on_first(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def add_on_last(self, data):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        new_node = Node(data=data)
        temp.next = new_node


    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("This node doesn't exist in DLL")

        new_node = Node(data=new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def print_llist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    llist = DoublyLinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.print_llist()

    llist.add_on_first(0)

    print()
    llist.print_llist()

    llist.add_on_last(4)
    print()
    llist.print_llist()