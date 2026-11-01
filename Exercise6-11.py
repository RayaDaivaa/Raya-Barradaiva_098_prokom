cities = {'surakarta':
        {'country': 'indonesia',
        'population': 2400000,
        'fact': 'Known for its traditional batik.'},
    'tokyo': 
    {'country': 'japan',
        'population': 1250000,
        'fact': 'Known for its modern technology.'},
    'paris':
    {'country': 'france',
        'population': 20000,
        'fact': 'Known for the Eiffel Tower.'}}

for city, information in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {information['country'].title()}")
    print(f"Population: {information['population']:,}")
    print(f"Fact: {information['fact']}")