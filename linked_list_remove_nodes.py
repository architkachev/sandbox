class LinkedList(object):
    class Node(object):
        def __init__(self, item, prev_item, next_item):
            self.next_item = next_item
            self.prev_item = prev_item
            self.item = item

        def __str__(self):
            return "({0} <- {1} -> {2})".format(self.prev_item
                if self.prev_item is None else self.prev_item.item,
                                                self.item,
                                                self.next_item
                if self.next_item is None else self.next_item.item)

    class LinkedListIterator(object):
        def __init__(self, linked_list):
            self.linked_list = linked_list
            self.current = linked_list.first_node

        def __iter__(self):
            return self

        def next(self):
            if self.linked_list.is_empty():
                raise StopIteration
            else:
                if self.current is None:
                    raise StopIteration
                res = self.current
                self.current = self.current.next_item
                return res

        def has_next(self):
            return self.current.next_item is not None

    def __iter__(self):
        return LinkedList.LinkedListIterator(self)

    def __init__(self):
        self.first_node = None
        self.end_node = None

    def index(self):
        pass

    def insert(self, i, x):
        pass

    def remove(self, x):
        if self.is_empty():
            return
        else:
            current = self.first_node
            while True:
                if current.item == x:
                    if current.prev_item is None:
                        current.next_item.prev_item = None
                    elif current.next_item is None:
                        current.prev_item.next_item = None
                    else:
                        current.prev_item.next_item = current.next_item
                        current.next_item.prev_item = current.prev_item
                if current.next_item is None:
                    break
                else:
                    current = current.next_item

    def append(self, x):
        if self.first_node is None and self.end_node is None:
            self.first_node = self.end_node = LinkedList.Node(x, None, None)
        else:
            new_item = LinkedList.Node(x, self.end_node, None)
            self.end_node.next_item = new_item
            self.end_node = new_item

    def reverse(self):
        pass

    def pop(self, i=-1):
        pass

    def extend(self, t):
        pass

    def count(self, x):
        pass

    def sort(self, cmp=None, key=None, reverse=False):
        pass

    def is_empty(self):
        return self.first_node is None and self.end_node is None

    def __str__(self):
        res = ""
        for i in self:
            res += str(i) + "\n"
        return res


ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(1)
ll.append(1)
ll.append(4)
ll.append(5)
ll.append(5)
ll.append(1)
ll.append(5)
ll.append(6)
ll.append(6)
ll.append(6)

print ll

    #
    # ll.print_list()
    # print ""
    #
    # ll.remove(1)
    #
    # ll.print_list()
