from pyfirmata import Arduino
import time

if __name__ == '__main__':
    board = Arduino('COM4')
    print('Communication Successfully started')

    while True:
        board.digital[13].write(1)
        time.sleep(2)
        board.digital[13].write(0)
        time.sleep(1)