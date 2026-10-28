
tree = [None] * 100

def insert():
    x = int(input("Enter value: "))

    if tree[0] is None:
        tree[0] = x
        print("Node inserted")
        return

    p = int(input("Enter parent index: "))
    if p < 0 or p >= 100 or tree[p] is None:
        print("Invalid parent")
        return

    ch = input("Enter L for left or R for right: ").upper()

    if ch == 'L':
        i = 2 * p + 1
    elif ch == 'R':
        i = 2 * p + 2
    else:
        print("Invalid choice")
        return

    if i >= 100:
        print("Tree is full")
    elif tree[i] is not None:
        print("Position already occupied")
    else:
        tree[i] = x
        print("Node inserted")


def search():
    x = int(input("Enter value to search: "))
    for i in range(100):
        if tree[i] == x:
            print("Node found at index", i)
            return
    print("Node not found")


def delete():
    x = int(input("Enter value to delete: "))

    for i in range(100):
        if tree[i] == x:
            tree[i] = None
            print("Node deleted")
            return

    print("Node not found")


def display():
    print("Array representation:")
    print(tree)


def preorder(i):
    if i < 100 and tree[i] is not None:
        print(tree[i], end=" ")
        preorder(2 * i + 1)
        preorder(2 * i + 2)


def inorder(i):
    if i < 100 and tree[i] is not None:
        inorder(2 * i + 1)
        print(tree[i], end=" ")
        inorder(2 * i + 2)


def postorder(i):
    if i < 100 and tree[i] is not None:
        postorder(2 * i + 1)
        postorder(2 * i + 2)
        print(tree[i], end=" ")


while True:
    print("\n\n1.Insert")
    print("2.Delete")
    print("3.Search")
    print("4.Display")
    print("5.Preorder")
    print("6.Inorder")
    print("7.Postorder")
    print("8.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        insert()
    elif ch == 2:
        delete()
    elif ch == 3:
        search()
    elif ch == 4:
        display()
    elif ch == 5:
        preorder(0)
    elif ch == 6:
        inorder(0)
    elif ch == 7:
        postorder(0)
    elif ch == 8:
        break
    else:
        print("Invalid choice")
