
queue = []
size = int(input("Enter queue size: "))
front = -1
rear = -1

def enqueue():
    global front, rear

    if (rear + 1) % size == front:
        print("Circular Queue Overflow")
        return

    element = int(input("Enter element: "))

    if front == -1:
        front = 0

    rear = (rear + 1) % size
    if len(queue) < size:
        queue.append(None)
    queue[rear] = element

    print("Element inserted:", element)

def dequeue():
    global front, rear

    if front == -1:
        print("Circular Queue Underflow")
        return

    print("Deleted element:", queue[front])

    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % size

def peek():
    if front == -1:
        print("Circular Queue is empty")
    else:
        print("Front element:", queue[front])

def display():
    if front == -1:
        print("Circular Queue is empty")
        return

    print("Circular Queue elements:", end=" ")
    i = front

    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size

    print()

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
