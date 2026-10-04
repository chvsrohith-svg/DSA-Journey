# Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        self.head = None
        temp = None

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                temp = new_node
            else:
                temp.next = new_node
                temp = new_node

        print("Linked list created successfully.")

    # 2. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print("Node inserted at beginning.")

    # 3. Insert at End
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

        print("Node inserted at end.")

    # 4. Insert at Index
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
            self.head = new_node
            print("Node inserted.")
            return

        temp = self.head

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
        temp.next = new_node

        print("Node inserted at index", index)

    # 5. Delete by Value
    def delete_by_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("Linked list is empty.")
            return

        # If first node contains the value
        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted.")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("Node deleted.")
                return

            temp = temp.next

        print("Value not found.")

    # 6. Delete First Node
    def delete_first(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        self.head = self.head.next
        print("First node deleted.")

    # 7. Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

        print("Last node deleted.")

    # 8. Count Number of Nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        print("Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program

linked_list = SinglyLinkedList()

while True:
    print("\n========== SINGLY LINKED LIST ==========")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        linked_list.create()

    elif choice == 2:
        linked_list.insert_beginning()

    elif choice == 3:
        linked_list.insert_end()

    elif choice == 4:
        linked_list.insert_at_index()

    elif choice == 5:
        linked_list.delete_by_value()

    elif choice == 6:
        linked_list.delete_first()

    elif choice == 7:
        linked_list.delete_last()

    elif choice == 8:
        linked_list.count_nodes()

    elif choice == 9:
        linked_list.display()

    elif choice == 10:
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please try again.")
