# Реализовать упорядоченный связный список.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'Data: {self.data}. Next node object: {self.next.data}'


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_llist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def sort_it(self):
        i = 0
        while i is not self.l_len():
            i += 1
            self.get_sort()

    def l_len(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def get_sort(self):
        sup_prev = None
        prev = None
        cur = self.head
        while cur.next:
            if cur.next:
                sup_prev = prev
                prev = cur
                cur = cur.next
                if cur.data < prev.data:
                    prev.next = cur.next
                    cur.next = prev
                    if not sup_prev:
                        self.head = cur
                    else:
                        sup_prev.next = cur

                        x = cur
                        cur = prev
                        prev = x


llist = LinkedList()
llist.push(33)
llist.push(28)
llist.push(31)
llist.push(49)
llist.push(50)
llist.push(66)
llist.push(71)
llist.push(82)
llist.push(90)
llist.print_llist()

llist.sort_it()

print()
llist.print_llist()

