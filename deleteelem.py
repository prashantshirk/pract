from array import array
arr = array('i', [10, 20, 30, 40, 50])

pos = int(input("Enter position to delete (0-based index): "))

# Check to make sure the position exists before trying to remove it
if 0 <= pos < len(arr):
  # The function that removes the car at the given position
  arr.pop(pos)
  print("Array after deletion:", arr.tolist())
else:
  print("Invalid position!")