# Реализовать работу очереди (добавление/удаление элементов) на основе связного списка.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'Data: {self.data}. Next node object: {self.next.data}'


class Queue:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def dell(self):
        prev = None
        curr = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None
        del curr

    def print_llist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.print_llist()
q.dell()
print()
q.print_llist()