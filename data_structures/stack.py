# Реализовать постфиксную форму для операций умножения и сложения используя стек.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def count(self):
        l = []
        for item in self.items:
            if isinstance(item, int):
                l.append(item)

        for item in self.items:
            if item is '+':
                x = l.pop(0)
                y = l.pop(0)
                sum = x + y
                l.insert(0, sum)
            elif item is '*':
                x = l.pop(0)
                y = l.pop(0)
                res = x * y
                l.insert(0, res)
        else:
            return l.pop()


a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push('+')
a.push('*')
print(a.items)
print(a.count())
