stack = []
size = int(input("Enter stack size: "))

def push():
    if len(stack) >= size:
        print("Stack Overflow")
    else:
        element = int(input("Enter element: "))
        stack.append(element)
        print("Element pushed:", element)

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        print("Popped element:", stack.pop())

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

def display():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack elements:", stack[::-1])

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        push()
    elif choice == "2":
        pop()
    elif choice == "3":
        peek()
    elif choice == "4":
        display()
    elif choice == "5":
        print("Program terminated")
        break
    else:
        print("Invalid choice")
