def build_profile(first, last, **user_info): 
    """Build a dictionary containing everything we know about a user.""" 
    user_info['first_name'] = first 
    user_info['last_name'] = last 
    return user_info 
user_profile = build_profile('Margaret', 'Adeniran', 
                             location='Lagos', 
                             field='Machine Learning',
                             fav_food='Amala') 
print(user_profile)