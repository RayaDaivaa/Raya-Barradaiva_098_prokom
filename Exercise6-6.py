favorite_languages = {
    'tiara': 'python',
    'sarah': 'c',
    'nasya': 'rust',
    'iqbal': 'python'}

people = ['afifah', 'radinka', 'nasya', 'tiara', 'renaya']

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding!")
    else:
        print(f"{person.title()}, please take the poll.")