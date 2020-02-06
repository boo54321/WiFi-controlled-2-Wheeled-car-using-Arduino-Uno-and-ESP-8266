# WiFi-controlled-2-Wheeled-car-using-Arduino-Uno-and-ESP-8266
This Repository Contains Two files besdies this readme, they are
  1. RcFinal.py
  2. FinalCode.ino

## RcFinal.py
This will act as the server which will connect to the ESP8266 module which inturn will send directions to arduino to follow
Dependency: PySimpleGUI, Keyboard, time, Socket, time, tkinter

## FinalCode.ino
This is a Arduino Code to act as client. This code uses the ESP8266 to create a hotspot and then allow users to connect to it 
Dependency : ESP8266_Lib.h and ESP8266.cpp.  Import it and work

Feel free to create a application of RcFinal.py via PyInstaller, Platypus, etc 
