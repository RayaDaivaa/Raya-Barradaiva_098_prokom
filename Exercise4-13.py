foods = ('rice', 'chicken', 'soup', 'salad', 'ice cream')

print("Original menu:")
for food in foods:
    print(food)

# Mencoba mengubah tuple.
try:
    foods[0] = 'noodles'
except TypeError:
    print("\nTuple cannot be modified!")

# Mengganti seluruh isi tuple.
foods = ('noodles', 'fish', 'soup', 'salad', 'cake')

print("\nRevised menu:")
for food in foods:
    print(food)