SIZE = 10
table = [[] for _ in range(SIZE)]

def insert(key):
    index = key % SIZE
    table[index].append(key)
    print("Inserted successfully")

def search(key):
    index = key % SIZE

    if key in table[index]:
        print("Element found")
    else:
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
