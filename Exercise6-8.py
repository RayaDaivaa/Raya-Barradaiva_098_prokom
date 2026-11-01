pet_1 = {
    'animal': 'cat',
    'owner': 'barra'}

pet_2 = {
    'animal': 'dog',
    'owner': 'adit'}

pet_3 = {
    'animal': 'rabbit',
    'owner': 'dhirga'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")