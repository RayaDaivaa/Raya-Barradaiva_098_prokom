people = {'raya': 
          {'full_name': 'Raya Daiva',
        'age': '18',
        'city': 'Surakarta',
        'education': 'Senior High School',
        'hobby': 'Learning programming',
        'job': 'Student'},
    'juna':
    {'full_name': 'Juna Pratama',
        'age': '18',
        'city': 'Sukoharjo',
        'education': 'Senior High School',
        'hobby': 'Playing football',
        'job': 'Student'}}

for username, information in people.items():
    print(f"\nUsername: {username}")
    print(f"Name: {information['full_name']}")
    print(f"Age: {information['age']}")
    print(f"City: {information['city']}")
    print(f"Education: {information['education']}")
    print(f"Hobby: {information['hobby']}")
    print(f"Job: {information['job']}")