
class Node:
        def __init__(self, value):
                self.value = value
                self.next = None

class LinkedLists:
        def __init__(self, value):
                new_node = Node(value)
                self.head = new_node
                self.tail = new_node
                self.length = 1

        def print_list(self):
                temp = self.head
                while temp is not None:
                        print(temp.value)
                        temp = temp.next
        def make_empty(self):
                self.head = None
                self.tail = None
                self.length = 0

        def append(self, value):
                new_node = Node(value)
                if self.head is None:
                        self.head = new_node
                        self.tail = new_node
                else:
                        self.tail.next = new_node
                        self.tail = new_node
                self.length += 1
        def pop(self):
                if self.length == 0:
                        return None
                
                temp = self.head
                pre = self.head
                while temp.next:
                        pre = temp
                        temp = temp.next
                self.tail = pre
                self.tail.next = None
                self.length -=1

                if self.length == 0:
                        self.head = None
                        self.tail = None
                return temp
        
        def prepend(self, value):
                new_node = Node(value)
                if self.length == 0:
                        self.head = new_node
                        self.tail = new_node
                else:
                        new_node.next = self.head
                        self.head = new_node
                self.length += 1

        def pop_first(self):
                if self.length == 0:
                        return None
                temp = self.head
                self.head = self.head.next
                temp.next = None
                self.length -= 1
                if self.length == 0:
                        self.tail = None
                return temp


        def get(self, index):
                if index < 0 or index >= self.length:
                        return None
                temp = self.head
                for _ in range(index):
                        temp = temp.next
                return temp
        
        def set_value(self, index, value):
                temp = self.get(index)
                if temp:
                        temp.value = value
                        return True
                return False
        def insert(self, index, value):
                if index < 0 or index > self.length:
                        return False
                if index == 0:
                        self.prepend(value)
                        return True
                if index == self.length:
                        self.append(value)
                        return True
                new_node = Node(value)
                temp = self.get(index - 1)
                new_node.next = temp.next
                temp.next = new_node
                self.length += 1
                return True
        
        def remove(self, index):
                if index < 0 or index >= self.length:
                        return None
                if index == 0:
                        return self.pop_first()
                if index == self.length - 1:
                        return self.pop()
                pre = self.get(index - 1)
                temp = pre.next
                pre.next = temp.next
                temp.next = None
                self.length -= 1
                return temp
        
        def reverse(self):
                temp = self.head
                self.head = self.tail
                self.tail = temp
                after = temp.next
                before = None
                for _ in range(self.length):
                        after = temp.next
                        temp.next = before
                        before = temp
                        temp = after



my_linked_list = LinkedLists(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print("Befor reverse:")
my_linked_list.print_list()

my_linked_list.reverse()

print("\nAfter reverse:")
my_linked_list.print_list()








# my_linked_list = LinkedLists(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# print("Head:", my_linked_list.head.value)
# print("Tail:", my_linked_list.tail.value)
# print("Length:", my_linked_list.length)

# print("\nLinked List:")
# my_linked_list.print_list()

# print("\nAfter adding 4 node")
# my_linked_list.append(4)


# print("Head:", my_linked_list.head.value)
# print("Tail:", my_linked_list.tail.value)
# print("Length:", my_linked_list.length)
# print("\nLinked List:")
# my_linked_list.print_list()

# print("Before pop:")
# my_linked_list.print_list()

# popped_node = my_linked_list.pop()
# print(f"\nPopped value: {popped_node.value}\n")

# print("After pop:")
# my_linked_list.print_list()

# my_linked_list.append(3)
# print("Before prepend()")
# print("-" * 20)
# print(f"Head:", my_linked_list.head.value)
# print(f"Tail:", my_linked_list.tail.value)
# print(f"Length:", my_linked_list.length)
# print(f"\nLinked list:")
# my_linked_list.print_list()

# my_linked_list.prepend(1)
# print("\nAfter prepend()")
# print("-" * 20)
# print(f"Head:", my_linked_list.head.value)
# print(f"Tail:", my_linked_list.tail.value)
# print(f"Length:", my_linked_list.length)
# print(f"\nLinked List:")

# my_linked_list = LinkedLists(2)
# my_linked_list.append(1)
# # (2) Items - return 2
# print(my_linked_list.pop_first().value)
# # (1) Items - returne 1 Node
# print(my_linked_list.pop_first().value)
# # (0) Items - returne None
# print(my_linked_list.pop_first())

# my_linked_list = LinkedLists(2)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# result = my_linked_list.get(2).value
# print(result)

# my_linked_list = LinkedLists(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# print("Before:")
# my_linked_list.print_list()

# my_linked_list.set_value(1, 4)
# print("\nAfter:")
# my_linked_list.print_list()


# my_linked_list = LinkedLists(2)
# my_linked_list.prepend(0)

# print("Before insert():")
# my_linked_list.print_list()

# my_linked_list.insert(1, 1)
# print("\nAfter insert():")
# my_linked_list.print_list()


# my_linked_list = LinkedLists(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# print("Before remove():")
# my_linked_list.print_list()

# my_linked_list.remove(2)
# print("\nAfter remove():")
# my_linked_list.print_list()
