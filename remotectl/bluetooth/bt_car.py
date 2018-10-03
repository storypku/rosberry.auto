import bluetooth
import RPi.GPIO as gpio
from time import sleep

def gpio_init():
    """Setup GPIO numbering mode and define output pins"""
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def cleanup():
    gpio.cleanup()

def forward():
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)

def backward():
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)

def turn_left():
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)

def turn_right():
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)

def stop():
    gpio.output(17, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)

def bt_one():
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    sock.bind(("", port))
    sock.listen(1)
    client, address = sock.accept()
    print ("Accept conection from " + str(address))
    return client

if __name__ == "__main__":
    gpio_init()
    try:
        btclient = bt_one()
        while True:
            msg = btclient.recv(1024)
            print("Received msg: {}".format(msg))
            if msg == "B" or msg == "b":
                backward()
                sleep(1)
                stop()
            elif msg == "F" or msg == "f":
                forward()
                sleep(1)
                stop()
            elif msg == "R" or msg == "r":
                turn_right()
                sleep(1)
                stop()
            elif msg == "L" or msg == "l":
                turn_left()
                sleep(1)
                stop()
            elif msg == "Z" or msg == "z":
                stop()
            elif msg == "Q" or msg == "q":
                btclient.close()
                btserver.close()
                break
            else:
                print("Unknown command: " + msg)
    finally:
        cleanup()

