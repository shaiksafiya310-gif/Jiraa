numbers = [10, 20, 30, 40, 50, 60]

print("Original List:", numbers)
element = int(input("Enter the element to remove: "))

if element in numbers:
    numbers.remove(element)
    print("Element removed successfully")
else:
    print("Element not found in the list")

print("Updated List:", numbers)

print("Remaining elements are:")
for i in numbers:
    print(i)