
import RPi.GPIO as GPIO
import dht11

def dht11Func():
  # initialize GPIO 
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

  # read data using pin 14
  instance = dht11.DHT11(pin = 4)
  result = instance.read()

  # while the values aren't correct or even available
  while not result.is_valid():
    # retrieve the data
    result = instance.read()
  
  # variable description with measurement data
  temperature = result.temperature
  humidity = result.humidity
  # cleanup the GPIO for clean reuse
  GPIO.cleanup()
	
  return [temperature, humidity]
