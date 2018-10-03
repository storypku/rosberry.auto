import curses
import RPi.GPIO as gpio
from time import sleep

screen = None

def gpio_init():
    """Setup GPIO numbering mode and define output pins"""
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def screen_init():
    """
    Get the curses window, turn off echoing of keyboard to screen,
    turn on instant (no waiting) key response, and use special
    values for cursor keys
    """
    global screen
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

def cleanup():
    """
    Close down curses properly, inc turn echo back on!
    """
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
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

    
if __name__ == "__main__":
    gpio_init()
    screen_init()
    try:
        while True:
            character = screen.getch()
            if character == ord('q'):
                break
            elif character == curses.KEY_UP:
                forward()
            elif character == curses.KEY_DOWN:
                backward()
            elif character == curses.KEY_LEFT:
                turn_left()
            elif character == curses.KEY_RIGHT:
                turn_right()
            elif character == 10: # \n
                stop()

    finally:
        cleanup()

