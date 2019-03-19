"""
This program finds the hour with the cheapest electricity tariff price
and turns an eco plug off during this hour.

Author: Caleb Shelton, UEA Arduino Innovator
"""

import serial
from datetime import datetime
import time

# Open a serial connection on port COM4 with baudrate 115200
ser1 = serial.Serial('COM4', 115200)

# List of today's tariff data with the first item being between the hours:
# 00-01 and the last: 23-00
todays_tariff = [
                 38.09,
                 43.36,
                 39.99,
                 37.71,
                 37.01,
                 37.63,
                 41.81,
                 44.40,
                 57.81,
                 60.00,
                 57.73,
                 50.90,
                 44.50,
                 45.00,
                 37.98,
                 36.79,
                 37.13,
                 40.11,
                 46.72,
                 60.42,
                 55.51,
                 44.50,
                 40.91,
                 36.90,
                      ]

# Find the smallest value in the list (cheapest hour)
x = min(float(t) for t in todays_tariff)

# Find the index position of the cheapest hour in the list which
# corresponds to the hour to schedule the plug to be on for
scheduled_hour = todays_tariff.index(x)

# Loop forever, checking if the current hour is the scheduled hour, if it is
# then turn on the plug. Wait an hour then turn it back on
while True:
    current_hour = datetime.now().hour

    if current_hour == scheduled_hour:
        ser1.write('s'.encode())
        time.sleep(3600) #3600 seconds = 1 hour
        ser1.write('s'.encode())
