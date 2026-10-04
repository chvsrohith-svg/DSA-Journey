n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)


for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            # Swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)
