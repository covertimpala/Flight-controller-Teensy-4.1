import serial
import time
from plyer import notification
import pyautogui
global err
err = 0
def serialcomm():
    global err
    global ser
    try:
        ser=serial.Serial("COM3",9600)  #change ACM number as found from ls /dev/tty/ACM*
        global line
        def sensors():
            global line
            line = ser.readline()  #reads serial communications
        global check
        check = ""
        print("started")
        while True:
            sensors()
            if check != line:
                check = line
                print(line)
                if "1 pressed" in str(line):
                    pyautogui.hotkey("ctrlleft", "a")
            time.sleep(.1)
    except Exception as e:
        if "ClearCommError failed" in str(e) or "could not open port" in str(e):
            if err != 1:
                print("waiting for connection...")
                err = 1
                
            #com()
        else:
            print(e)

#def com():
    #while True:
        #try:
            #ser=serial.Serial("COM3",9600)
            #ser.readline()
            #break
        #except Exception as e:
            #time.sleep(.1)
            #print(e)
    #serialcomm()
while True:
    serialcomm()