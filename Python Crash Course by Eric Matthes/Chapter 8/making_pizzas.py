'''import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')'''

#module_name.function_name()
#For importing specific funtions; from module_name import funtion_0, function_1, function_2

#Using as to give a function an alias; from module_name import function_name as fn
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to give a module an alias; import module_name as mn
#Importing all funtions in a module; from module_name import *


#Styling function
'''To specify a default value for a parameter; 
        def function_name(parameter_0, parameter_1='default value')'''
'''Use this also for keyword arguments;
        function_name(value_0, parameter_1='value')'''
'''If your function is really long;
        def function_name(
                parameter_0, parameter_1, parameter_2,
                parameter_3, parameter_4, parameter_5):
            funtion body...'''