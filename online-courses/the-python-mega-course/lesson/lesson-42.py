
def weather_condition(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

# also available is    temp = int(input('Enter temperature: '))
# but float is better
temp = float(input('Enter temperature: '))
weather = weather_condition(temp)
print(weather)