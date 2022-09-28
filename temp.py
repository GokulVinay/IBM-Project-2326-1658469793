from random import randint
def temp():
    return randint(1,100)
def humi():
    return randint(1,100)
random_temperature=temp()
print("Temperature is",random_temperature)
random_humidity=humi()
print("Humidity is",random_humidity)
if random_temperature not in range(5,30):
    print("caution! high temperature!!")
else:
    print("temperature is normal")
if random_humidity not in range(30,60):
    print("caution! humidity is high")
else:
    print("humidity is normal")
