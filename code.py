import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import busio
import struct
import time
import usb_cdc
from rainbowio import colorwheel
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pixel_pin = board.A6
num_pixels = 8
pixels = neopixel.NeoPixel(board.A6, 8, brightness=0.1, auto_write=False)

RED = (255, 0, 0)
YELLOW = (150, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

pixels[0] = (GREEN)
pixels[1] = (GREEN)
pixels[2] = (GREEN)
pixels[3] = (GREEN)
pixels[4] = (YELLOW)
pixels[5] = (YELLOW)
pixels[6] = (RED)
pixels[7] = (RED)

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # KeyboardLayoutUS(keyboard)

pixels.show()
#from adafruit_circuitplayground.express import cpx
serial = usb_cdc.data
print("help")
#uart = busio.UART(board.TX, board.RX, baudrate=9600)

led = digitalio.DigitalInOut(board.A9)
led.direction = digitalio.Direction.OUTPUT
led.value = True
#button1 = digitalio.DigitalInOut(board.D1)
#button1.direction = Direction.INPUT
#button1.pull = Pull.UP
##############################
keys = [Keycode.Q, Keycode.W, Keycode.E, Keycode.R, Keycode.T, Keycode.Y, Keycode.U, Keycode.I, Keycode.O, Keycode.P, Keycode.A, Keycode.S, Keycode.D, Keycode.F, Keycode.G, Keycode.H, Keycode.J]
button = {}

button[0] = digitalio.DigitalInOut(board.D1)
button[1] = digitalio.DigitalInOut(board.D2)
button[2] = digitalio.DigitalInOut(board.D3)
button[3] = digitalio.DigitalInOut(board.D4)
button[4] = digitalio.DigitalInOut(board.D5)
button[5] = digitalio.DigitalInOut(board.D6)
button[6] = digitalio.DigitalInOut(board.D7)
button[7] = digitalio.DigitalInOut(board.D8)
button[8] = digitalio.DigitalInOut(board.D9)
button[9] = digitalio.DigitalInOut(board.D10)
button[10] = digitalio.DigitalInOut(board.D11)

button[11] = digitalio.DigitalInOut(board.D33)
button[12] = digitalio.DigitalInOut(board.D34)
button[13] = digitalio.DigitalInOut(board.D35)
button[14] = digitalio.DigitalInOut(board.D36)
button[15] = digitalio.DigitalInOut(board.D37)
button[16] = digitalio.DigitalInOut(board.D38)

for v in range(len(button)):
	button[v].direction = Direction.INPUT
	button[v].pull = Pull.UP
##############################
time.sleep(1)
led.value = False
#i = 1
p = 1
toggled = {}
for i in range(len(button)):
     toggled[i] = False
#toggled[33] = "off"
#toggled[34] = "off"
#toggled[35] = "off"
#toggled[36] = "off"
#toggled[37] = "off"
#toggled[38] = "off"
while True:
    for pin in range(len(button)):
        if button[pin].value == False:
            if button[pin].value != toggled[pin]:
                 keyboard.press(keys[pin])
                 keyboard.release_all()
            toggled[pin] = False
        else:
            toggled[pin] = True
    time.sleep(0.01)
