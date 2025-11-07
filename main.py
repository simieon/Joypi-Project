from adafruit_ht16k33.segments import Seg7x4 
import time
import board
import busio

# imports functions from the other files
from dht11new import dht11Func
from sevenSeg import sevenSegmentDisplay
from lcd import show_data_on_lcd, shutdown_lcd

print("Please interrupt the program with 'STR C' to end it!")

# connection with the 7segment module
i2cSegment = board.I2C() 
segment = Seg7x4(i2cSegment, address=0x70)

while True :
  try:
    # initialize the function for data fetch
    data = dht11Func()
    temperature = int(data[0])
    humidity = int(data[1])

    # clears the displayed data
    segment.fill(0)
    # the function call with handover of the segment connection and the measurement data
    sevenSegmentDisplay(segment, str(humidity) + str(temperature))

    show_data_on_lcd(temperature=temperature, humidity=humidity)
    # 20sec waiting time before the loop repeats
    time.sleep(20)
  except KeyboardInterrupt:
    shutdown_lcd()
    segment.fill(0)
    break
