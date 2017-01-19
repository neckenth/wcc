def get_season(month):
    winter = ['dec', 'jan', 'feb']
    spring = ['mar', 'apr', 'may']
    summer = ['jun', 'jul', 'aug']
    fall = ['sep', 'oct', 'nov']

    if month.lower() in winter:
        return 'Winter'
    elif month.lower() in spring:
        return 'Spring'
    elif month.lower() in summer:
        return 'Summer'
    elif month.lower() in fall:
        return 'Fall'
    else:
        return 'Month not found'

# print get_season('jan') # Expected: Winter
# print get_season('Jan') # Expected: Winter
# print get_season('may') # Expected: Spring
# print get_season('aug') # Expected: Summer
# print get_season('sep') # Expected: Fall
# print get_season('sepp') # Expected: month not found


def get_celsius(temp_f):
    temp_c = (temp_f - 31) / 1.8
    return round(temp_c, 2)

#print get_celsius(55)


def get_fahrenheit(temp_c):
    temp_f = (temp_c * 1.8) + 32
    return round(temp_f, 2)

#print get_fahrenheit(10)


def temperature_converter(temp, convert_to):
    if convert_to == 'C':
        new_temp = get_celsius(temp)
        return new_temp
    elif convert_to == 'F':
        new_temp = get_fahrenheit(temp)
        return new_temp
    else:
        return 'Error: Invalid temperature scale; Must be F or C.'

#print temperature_converter(55, 'C')
#print temperature_converter(10, 'F')
#print temperature_converter(55, 'X') # Error: Invalid temperature scale; Must be `F` or `C`


def vowel_counter(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for letter in string:
        if letter in vowels:
            counter += 1
        else:
            counter = counter
    return counter

# print vowel_counter('apples') # Expected: 2
# print vowel_counter('aeiou') # Expected: 5
# print vowel_counter('why') # Expected: 0
# print vowel_counter('mississippi') # Expected: 4

