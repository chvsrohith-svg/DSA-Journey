
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = None


def insert():
    global root
    x = int(input("Enter value: "))
    n = Node(x)

    if root is None:
        root = n
        print("Node inserted")
        return

    q = [root]

    while q:
        t = q.pop(0)

        if t.left is None:
            t.left = n
            print("Node inserted")
            return
        else:
            q.append(t.left)

        if t.right is None:
            t.right = n
            print("Node inserted")
            return
        else:
            q.append(t.right)


def search(t, x):
    if t is None:
        return None
    if t.data == x:
        return t

    a = search(t.left, x)
    if a:
        return a

    return search(t.right, x)


def delete():
    global root
    x = int(input("Enter value to delete: "))

    if root is None:
        print("Tree is empty")
        return

    q = [(root, None, None)]
    target = None
    last = None

    while q:
        t, p, side = q.pop(0)

        if t.data == x and target is None:
            target = (t, p, side)

        last = (t, p, side)

        if t.left:
            q.append((t.left, t, 'L'))
        if t.right:
            q.append((t.right, t, 'R'))

    if target is None:
        print("Node not found")
        return

    t, p, side = target
    last_node, last_parent, last_side = last

    t.data = last_node.data

    if last_parent is None:
        root = None
    elif last_side == 'L':
        last_parent.left = None
    else:
        last_parent.right = None

    print("Node deleted")


def display(t):
    if t:
        print(t.data, end=" ")
        display(t.left)
        display(t.right)


def preorder(t):
    if t:
        print(t.data, end=" ")
        preorder(t.left)
        preorder(t.right)


def inorder(t):
    if t:
        inorder(t.left)
        print(t.data, end=" ")
        inorder(t.right)


def postorder(t):
    if t:
        postorder(t.left)
        postorder(t.right)
        print(t.data, end=" ")


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
        x = int(input("Enter value to search: "))
        if search(root, x):
            print("Node found")
        else:
            print("Node not found")
    elif ch == 4:
        print("Tree elements:")
        display(root)
    elif ch == 5:
        preorder(root)
    elif ch == 6:
        inorder(root)
    elif ch == 7:
        postorder(root)
    elif ch == 8:
        break
    else:
        print("Invalid choice")

