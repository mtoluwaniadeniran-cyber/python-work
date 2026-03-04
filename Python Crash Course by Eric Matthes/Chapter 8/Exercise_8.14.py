def make_car(manufacturer, model , **car_info): 
    """Build a dictionary containing everything we know about a car.""" 
    car_info['manufacturer_name'] = manufacturer  
    car_info['model_name'] = model 
    return car_info 
car_profile = make_car('Tesla', 'MX350', 
                             colour='grey', 
                             feature='self-driving') 
print(car_profile)