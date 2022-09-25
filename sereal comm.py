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
                if "1  pressed" in str(line):
                    pyautogui.hotkey("!")
                if "2  pressed" in str(line):
                    pyautogui.hotkey("g")
                if "3  pressed" in str(line):
                    pyautogui.hotkey("#")
                if "4  pressed" in str(line):
                    pyautogui.hotkey(" ")
                if "5  pressed" in str(line):
                    pyautogui.hotkey("@")
                if "6  pressed" in str(line):
                    pyautogui.hotkey("?")
                if "7  pressed" in str(line):
                    pyautogui.hotkey("delete", "$")
                if "8  pressed" in str(line):
                    pyautogui.hotkey("delete", "£")
                if "9  pressed" in str(line):
                    pyautogui.hotkey("delete", "{")
                if "10  pressed" in str(line):
                    pyautogui.hotkey("delete", "}")
                    ###
                if "33  toggled on" in str(line):
                    pyautogui.hotkey("ctrlleft", ",")
                if "33  toggled off" in str(line):
                    pyautogui.hotkey("ctrlleft", ",")
                if "34  toggled on" in str(line):
                    pyautogui.hotkey("ctrlleft", "#")
                if "34  toggled off" in str(line):
                    pyautogui.hotkey("ctrlleft", "#")
                if "35  toggled on" in str(line):
                    pyautogui.hotkey("ctrlleft", "b")
                if "35  toggled on" in str(line):
                    pyautogui.hotkey("ctrlleft", "b")
                if "36  toggled on" in str(line):
                    pyautogui.hotkey("u")
                if "36  toggled off" in str(line):
                    pyautogui.hotkey("u")
                if "37  toggled on" in str(line):
                    pyautogui.hotkey("ctrlleft", "v")
                if "37  toggled off" in str(line):
                    pyautogui.hotkey("ctrlleft", "v")
                if "38  toggled on" in str(line):
                    pyautogui.hotkey("ctrlleft", "y")
                if "38  toggled off" in str(line):
                    pyautogui.hotkey("ctrlleft", "y")
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