
queue = []
size = int(input("Enter queue size: "))

def enqueue():
    if len(queue) >= size:
        print("Queue Overflow")
    else:
        element = int(input("Enter element: "))
        queue.append(element)
        print("Element inserted:", element)

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue.pop(0))

def peek():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements:", queue)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enqueue()
    elif choice == "2":
        dequeue()
    elif choice == "3":
        peek()
    elif choice == "4":
        display()
    elif choice == "5":
        print("Program terminated")
        break
    else:
        print("Invalid choice")
