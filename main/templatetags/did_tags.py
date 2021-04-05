from django import template

register = template.Library()

#https://docs.djangoproject.com/en/3.1/ref/templates/builtins/
#https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/

'''
Converts a float into a readable price with currency icon
'''
def price(value):

    value = float(value)
    value = round(value,2)

    float_str = str(value)
    float_split = float_str.split(".")

    int_str = float_split[0]
    decimal_str = float_split[1]

    if len(decimal_str) == 1:
        new_decimal = f'{decimal_str}0'

        new_price = f'£{int_str}.{new_decimal}'
        return new_price
    else:
        return f'£{float_str}'




register.filter('price', price)