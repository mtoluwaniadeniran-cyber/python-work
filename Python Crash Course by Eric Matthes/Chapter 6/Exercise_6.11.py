cities = {
    'Tokyo':{
        'Country': 'Japan',
        'Population': '37 million', 
        'Fact': "One of the world's safest cities.",
        },

    'Dehli':{
        'Country': 'India',
        'Population': '30-35 million', 
        'Fact': 'Home to the Qutub Minar, a UNESCO World Heritage site.',
        },

    'Shangai':{      
          'Country': 'China',
          'Population': '26-31 million', 
          'Fact': "Features the world's first and fastest commercial maglev train line."
        }
}

for city, details in cities.items():
    print(f"\nCity: {city}")

    for detail in details:
        print(f"{detail}: {details[detail]}")