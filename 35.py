nums = [1, 3, 5, 6]

target = int(input("Enter target value: "))

position = 0

while position < len(nums):
    if nums[position] >= target:
        break
    position += 1

print("Insert Position:", position)