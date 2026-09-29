import time
from hs3003 import HS3003

sensor = HS3003()

while True:
    t, h = sensor.read()
    print(f"Temp: {t:.1f} C Humidity: {h:.1f} %".format(t, h))
    time.sleep(2)
    t2, h = sensor.read()
    print(f"Temp: {t2:.1f} C Humidity: {h:.1f} %".format(t, h))
    time.sleep(2)
    t3, h = sensor.read()
    print(f"Temp: {t3:.1f} C Humidity: {h:.1f} %".format(t, h))
    time.sleep(2)
    t4, h = sensor.read()
    print(f"Temp: {t4:.1f} C Humidity: {h:.1f} %".format(t, h))
    time.sleep(2)
    t5, h = sensor.read()
    print(f"Temp: {t5:.1f} C Humidity: {h:.1f} %".format(t, h))
    time.sleep(2)

    if t >= 7 and t <= 10:
        print("The temperature is low.")
        
    if t >= 11 and t <= 23:
        print("The themperture is normal.")
        
    if t >= 24 and t <= 35:
        print("The temperatue is high.")
        
    TempAverage= (t + t2 + t3 + t4 + t5)/5
    print(f"The TempAverage is: {TempAverage}")