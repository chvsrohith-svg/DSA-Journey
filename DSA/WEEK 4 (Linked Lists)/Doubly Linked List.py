# Doubly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # 1. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    # 2. Insert at End
    def insert_end(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Node inserted at end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

        print("Node inserted at end.")

    # 3. Insert at Index
    def insert_at_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter value: "))

        if index < 0:
            print("Invalid index.")
            return

        # Insert at beginning
        if index == 0:
            new_node = Node(data)

            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node

            print("Node inserted.")
            return

        temp = self.head

        # Move to node before the required index
        for i in range(index - 1):
            if temp is None:
                print("Invalid index.")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index.")
            return

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print("Node inserted at index", index)

    # 4. Delete by Value
    def delete_by_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        while temp is not None:

            if temp.data == value:

                # If deleting first node
                if temp.prev is None:
                    self.head = temp.next

                    if self.head is not None:
                        self.head.prev = None

                # If deleting any other node
                else:
                    temp.prev.next = temp.next

                    if temp.next is not None:
                        temp.next.prev = temp.prev

                print("Node deleted.")
                return

            temp = temp.next

        print("Value not found.")

    # 5. Delete First Node
    def delete_first(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("First node deleted.")

    # 6. Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        # Only one node
        if temp.next is None:
            self.head = None
            print("Last node deleted.")
            return

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

        print("Last node deleted.")

    # 7. Display Forward Nodes
    def display_forward(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        print("Forward: ", end="")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # 8. Display Backward Nodes
    def display_backward(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        # Move to last node
        while temp.next is not None:
            temp = temp.next

        print("Backward: ", end="")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# Main Program

dll = DoublyLinkedList()

while True:

    print("\n========== DOUBLY LINKED LIST ==========")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Index")
    print("4. Delete by Value")
    print("5. Delete First Node")
    print("6. Delete Last Node")
    print("7. Display Forward Nodes")
    print("8. Display Backward Nodes")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.insert_beginning()

    elif choice == 2:
        dll.insert_end()

    elif choice == 3:
        dll.insert_at_index()

    elif choice == 4:
        dll.delete_by_value()

    elif choice == 5:
        dll.delete_first()

    elif choice == 6:
        dll.delete_last()

    elif choice == 7:
        dll.display_forward()

    elif choice == 8:
        dll.display_backward()

    elif choice == 9:
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please try again.")
