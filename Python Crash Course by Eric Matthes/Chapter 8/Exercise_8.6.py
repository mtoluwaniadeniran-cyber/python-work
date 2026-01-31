def city_country(city_name, country_name):
    """Display a city and its country"""
    city_country = f"{city_name}, {country_name}."
    return city_country.title()

place = city_country('lagos', 'nigeria')
place_01 = city_country('dublin', 'ireland')
place_02 = city_country('nairobi', 'kenya')
print(place)
print(place_01)
print(place_02)