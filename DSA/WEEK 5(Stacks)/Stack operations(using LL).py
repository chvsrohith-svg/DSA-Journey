class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Element pushed:", data)

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Popped element:", self.top.data)
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top
            print("Stack elements:")
            while current is not None:
                print(current.data)
                current = current.next


s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        element = int(input("Enter element: "))
        s.push(element)
    elif choice == "2":
        s.pop()
    elif choice == "3":
        s.peek()
    elif choice == "4":
        s.display()
    elif choice == "5":
        print("Program terminated")
        break
    else:
        print("Invalid choice")
