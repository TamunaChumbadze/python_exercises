
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


my_linked_list = LinkedLists(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

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

print("Before pop:")
my_linked_list.print_list()

popped_node = my_linked_list.pop()
print(f"\nPopped value: {popped_node.value}\n")

print("After pop:")
my_linked_list.print_list()