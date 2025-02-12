class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

def get_input():
    while True:
        user_input = input("ievadi numuru: ")
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("nav numurs")


initial_value = get_input()
my_linked_list = LinkedList(initial_value)

while True:
    user_input = input("ievadi numuru: ")
    if user_input.lower() == 'break':
        break
    try:
        value = int(user_input)
        my_linked_list.append(value)
    except ValueError:
        print("nav numurs")

middle_node = my_linked_list.find_middle_node()

print("Middle number:", middle_node.value)


# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
# my_linked_list.append(6)
# 
# 
# middle_node = my_linked_list.find_middle_node()
# 
# print(middle_node.value)