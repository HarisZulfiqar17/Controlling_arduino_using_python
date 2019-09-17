import pyfirmata
import time
board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

o = board.get_pin('d:3:p')
i = board.get_pin('a:0:i')
for x in range(int(1)):
  time.sleep(1)
  o.write(0.3)
  time.sleep(1)
  print(i.read())
      
