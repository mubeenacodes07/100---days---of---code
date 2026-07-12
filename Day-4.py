fruits = ["apple", "banana", "mango", "orange"]
print("Starting list:", fruits)

removed_fruit = fruits.pop(1)
print("\nRemoved by pop(1):", removed_fruit)
print("After pop:", fruits)

fruits.remove("orange")
print("\nAfter remove('orange'):", fruits)

last_item = fruits.pop()
print("\nLast item popped:", last_item)
print("Final list:", fruits)

print("\nTotal fruits left:", len(fruits))
