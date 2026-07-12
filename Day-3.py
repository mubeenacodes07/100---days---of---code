fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40, 50]

print("Fruits list:", fruits)
print("Numbers list:", numbers)

print("\nFirst fruit:", fruit[0])
print("Last number:", number[-1])

fruit.append("orange")
print("\nAfter append:", fruits)

print("\nTotal fruits:", len(fruits))

print("\nAll fruits one by one:")
for fruit in fruits:
  print(fruit)
