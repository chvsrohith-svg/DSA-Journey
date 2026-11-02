SIZE = 10
table = [-1] * SIZE

def insert(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i * i) % SIZE

        if table[pos] == -1:
            table[pos] = key
            print("Inserted successfully")
            return

    print("Insertion failed")

def search(key):
    index = key % SIZE

    for i in range(SIZE):
        pos = (index + i * i) % SIZE

        if table[pos] == -1:
            break

        if table[pos] == key:
            print("Element found at index", pos)
            return

    print("Element not found")

def display():
    for i in range(SIZE):
        print(i, ":", table[i])

while True:
    print("\n1.Insert 2.Search 3.Display 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        insert(key)

    elif ch == 2:
        key = int(input("Enter key: "))
        search(key)

    elif ch == 3:
        display()

    elif ch == 4:
        break

    else:
        print("Invalid choice")
