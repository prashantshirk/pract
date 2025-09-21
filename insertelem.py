from array import array
# This is our starting train
arr=array('i', [10, 20, 30, 40, 50])

elem = int(input("Enter element to insert: "))
pos = int(input("Enter position (0-based index):"))

# The key function that adds the new car at the right spot
arr.insert(pos, elem)

print("Array after insertion:", arr.tolist())
