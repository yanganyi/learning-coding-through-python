import time
import os
import pandas
import numpy


numpy.random.random(5)

while True:
    if os.path.exists("daily_temperature.csv"):
        data = pandas.read_csv("daily_temperature.csv")
        print(data.mean())
        print(data.mean()["st1"])
        print(data.mean()["st2"])
    else:
        print("File does not exist.")
    time.sleep(1)