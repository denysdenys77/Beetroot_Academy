# Реализовать поиск элемента в связном списке.
# Реализовать удаление элемента в связном списке.


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

    def find(self, data):
        temp = self.head
        while temp.data is not data:
            temp = temp.next
        else:
            print(temp)

    def delete_node(self, key):
        prev = None
        curr = self.head
        while curr:
            if curr.data == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next

    def print_llist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    print("Список создан: ")
    llist.print_llist()


    print('\nЭлемент найден: ')
    x = llist.find(3)


    print('\nЭлемент "1" удален.')
    llist.delete_node(1)
    llist.print_llist()
