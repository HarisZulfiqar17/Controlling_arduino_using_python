from pyfirmata import Arduino, util
import time

board = Arduino("COM7")

loopTimes = input('How many times would you like the LED to blink: ')
print("Blinking " + loopTimes + " times.")

for x in range(int(loopTimes)):
  board.digital[13].write(1)
  time.sleep(1)
  board.digital[13].write(0)
  time.sleep(0.5)
