
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Element inserted:", data)

    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            print("Deleted element:", self.front.data)
            self.front = self.front.next

            if self.front is None:
                self.rear = None

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            current = self.front
            print("Queue elements:", end=" ")

            while current is not None:
                print(current.data, end=" ")
                current = current.next

            print()


q = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        element = int(input("Enter element: "))
        q.enqueue(element)
    elif choice == "2":
        q.dequeue()
    elif choice == "3":
        q.peek()
    elif choice == "4":
        q.display()
    elif choice == "5":
        print("Program terminated")
        break
    else:
        print("Invalid choice")
