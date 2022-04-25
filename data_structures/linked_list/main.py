class Node(object):
    def __init__(self, data=None, next_data=None):
        self.data = data
        self.next_data = next_data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_data

    def set_data(self, data):
        self.data = data

    def set_next(self, next_data):
        self.next_data = next_data


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append_right(self, data):
        new_node = Node(data)
        current_node = self.head
        if not current_node:
            self.head = new_node
            return

        while current_node.get_next():
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def append_left(self, data):
        new_node = Node(data)
        current_node = self.head
        new_node.set_next(current_node)
        self.head = new_node

    def remove_left(self):
        current_node = self.head
        self.head = current_node.get_next()

    def remove_right(self):
        current_node = self.head
        while current_node.get_next().get_next():
            current_node = current_node.get_next()
        current_node.set_next(None)

    def show(self):
        current_node = self.head
        output = "["
        while current_node:
            output += str(current_node.get_data())
            current_node = current_node.get_next()
            if current_node:
                output += " -> "
        output += "]"
        return output

    def get_by_index(self, index):
        current_node = self.head
        count = 0
        while current_node:
            if count == index:
                return current_node.get_data()
            count += 1
            current_node = current_node.get_next()
        raise IndexError('list index out of range')

    def append_by_index(self, index, data):
        new_node = Node(data)
        current_node = self.head
        count = 0
        while current_node.get_next():
            if index == 0:
                self.append_left(data)
                return
            elif index == self.length():
                self.append_right(data)
                return
            elif count + 1 == index:
                the_node_after_cur = current_node.get_next()
                current_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            current_node = current_node.get_next()
        raise IndexError('list index out of range')

    def remove_by_index(self, index):
        current_node = self.head
        count = 0
        if not current_node:
            raise IndexError('list index out of range')
        while current_node.get_next():
            if index == 0:
                self.remove_left()
                return
            elif index == self.length():
                self.remove_right()
                return
            elif count + 1 == index:
                the_node_to_remove = current_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                current_node.set_next(the_node_after_removed)
                return
            count += 1

    def length(self):
        count = -1
        current_node = self.head
        if not current_node:
            return count

        while current_node:
            current_node = current_node.get_next()
            count += 1
        return count

    def reverse(self):
        prev_node = None
        cur_node = self.head
        while cur_node != None:
            next_node = cur_node.get_next()
            cur_node.set_next(prev_node)
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node


new_list = LinkedList()
[new_list.append_right(i) for i in range(1, 101)]
print(new_list.show())
