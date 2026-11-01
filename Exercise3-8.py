places = ["Japan", "Switzerland", "Turkey", "South Korea", "USA"]

print("Original list:")
print(places)

print("\nAlphabetical order:")
print(sorted(places))

print("\nOriginal list:")
print(places)

print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

print("\nOriginal list:")
print(places)

places.reverse()
print("\nReversed list:")
print(places)

places.reverse()
print("\nBack to original order:")
print(places)

places.sort()
print("\nAlphabetical order:")
print(places)

places.sort(reverse=True)
print("\nReverse alphabetical order:")
print(places)