import pyfirmata
import time
board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

sw = board.get_pin('d:6:i')

for x in range(int(120)):
  time.sleep(1)
  print(sw.read())
  
