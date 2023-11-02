
from test_lib import test, report
# adden opzoeken

def get_value(data: str, separator: str, position: int) -> str:
    
    splitted_strings = data.split(separator)
    
    if 0 <= position < len(splitted_strings):   
        value = splitted_strings[position]
        return value
    else:
        return "vul een geldig ID in!"


#gebruik:
data = 'muis,kat,hond,vogel,vis'
separator = ','
position = 4
result = get_value(data, separator, position)

expected = "muis"
calculated = get_value(data, separator, 0)
test('test_muis', expected, calculated)

expected = "vul een geldig ID in!"
calculated = get_value(data, separator, 16)
test('test_muis', expected, calculated)

report()



