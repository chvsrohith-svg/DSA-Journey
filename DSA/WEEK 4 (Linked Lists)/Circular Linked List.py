# Circular Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        self.head = None
        tail = None

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                tail = new_node
                new_node.next = self.head
            else:
                tail.next = new_node
                tail = new_node
                tail.next = self.head

        print("Circular linked list created successfully.")

    # 2. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print("Node inserted at beginning.")
            return

        tail = self.head

        while tail.next != self.head:
            tail = tail.next

        new_node.next = self.head
        self.head = new_node
        tail.next = self.head

        print("Node inserted at beginning.")

    # 3. Insert at End
    def insert_end(self):
        data = int(input("Enter value: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print("Node inserted at end.")
            return

        tail = self.head

        while tail.next != self.head:
            tail = tail.next

        tail.next = new_node
        new_node.next = self.head

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

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                tail = self.head

                while tail.next != self.head:
                    tail = tail.next

                new_node.next = self.head
                self.head = new_node
                tail.next = self.head

            print("Node inserted.")
            return

        if self.head is None:
            print("Invalid index.")
            return

        temp = self.head
        current_index = 0

        # Find node before the required index
        while current_index < index - 1:
            temp = temp.next
            current_index += 1

            if temp == self.head:
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

        # If only one node
        if self.head.next == self.head:
            if self.head.data == value:
                self.head = None
                print("Node deleted.")
            else:
                print("Value not found.")
            return

        # If head contains the value
        if self.head.data == value:
            tail = self.head

            while tail.next != self.head:
                tail = tail.next

            self.head = self.head.next
            tail.next = self.head

            print("Node deleted.")
            return

        # Search for the value
        temp = self.head

        while temp.next != self.head:
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

        # Only one node
        if self.head.next == self.head:
            self.head = None
            print("First node deleted.")
            return

        tail = self.head

        while tail.next != self.head:
            tail = tail.next

        self.head = self.head.next
        tail.next = self.head

        print("First node deleted.")

    # 7. Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head

        # Find second-last node
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

        print("Last node deleted.")

    # 8. Count Number of Nodes
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # 9(a). Display Head to Tail
    def display_head_to_tail(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        print("Head to Tail:", end=" ")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(Head)")

    # 9(b). Display Tail to Head
    def display_tail_to_head(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        # Store nodes in a list
        nodes = []
        temp = self.head

        while True:
            nodes.append(temp.data)
            temp = temp.next

            if temp == self.head:
                break

        print("Tail to Head:", end=" ")

        for i in range(len(nodes) - 1, -1, -1):
            print(nodes[i], end=" -> ")

        print("(Head)")


# Main Program

cll = CircularLinkedList()

while True:

    print("\n========== CIRCULAR LINKED LIST ==========")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display")
    print("   a. Head to Tail")
    print("   b. Tail to Head")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        cll.insert_beginning()

    elif choice == 3:
        cll.insert_end()

    elif choice == 4:
        cll.insert_at_index()

    elif choice == 5:
        cll.delete_by_value()

    elif choice == 6:
        cll.delete_first()

    elif choice == 7:
        cll.delete_last()

    elif choice == 8:
        cll.count_nodes()

    elif choice == 9:
        print("\na. Head to Tail")
        print("b. Tail to Head")

        sub_choice = input("Enter your choice: ")

        if sub_choice == 'a':
            cll.display_head_to_tail()

        elif sub_choice == 'b':
            cll.display_tail_to_head()

        else:
            print("Invalid choice.")

    elif choice == 10:
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please try again.")
