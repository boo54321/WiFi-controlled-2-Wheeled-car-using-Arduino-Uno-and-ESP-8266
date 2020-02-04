import socket
import keyboard as Key
import time
import PySimpleGUI as GUI
import time
import tkinter
import os
# os.p
GUI.change_look_and_feel('DarkAmber')
Layout = [
    [GUI.Text("Welcome :D", (450, 1), justification="center")],
    [GUI.Text("Status : Initializing", (450, 2), key="Initial", justification="center")],
    [GUI.Button("LEFT", target=(3, 150), pad=(55, 20), disabled=True, key="ButtonLeft"),
     GUI.Button("UP", target=(3, 300), pad=(55, 20), disabled=True, key="ButtonUP"),
     GUI.Button("RIGHT", target=(3, 450), pad=(55, 20), disabled=True, key="ButtonRight")]
]


Window = GUI.Window("Controller", Layout, size=(500, 150)).Finalize()

SockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
SockTCP.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
IP = None
Record = True
Buf = ""
Binded = False
while not Binded:
    Window.Refresh()
    # print(Events, Values)
    # Window["ButtonLeft"].Update(button_color=("black", "red"))
    try:
        SockTCP.bind(("192.168.4.2", 55860))
        Binded = True
    except:
        print("A")
        Window["Initial"].Update("Status : Please Connect To JetBooWifi or See if Port is Occupied")
        time.sleep(0.3)
    # Window.Refresh()
    # Window.Refresh()
Window["Initial"].Update("Status : Connecting ...")
while True:
    try:
        Window.Refresh()
        if Record:
            SockTCP.listen(1)
            SockTCP, IP = SockTCP.accept()
            Buf = SockTCP.recv(10)
            SockTCP.send(bytes(2))
            print(str(Buf))
            Record = False
            Window["Initial"].Update("Status : Connected ! ")
            # Window["ButtonLeft"].Update(color=("black", "red"))
            Window["ButtonLeft"].Update(disabled=False)
            Window["ButtonUP"].Update(disabled=False)
            Window["ButtonRight"].Update(disabled=False)

        # print(Window["Buttons"])
        #     SockTCP.settimeout(0.04)
        #     print("UP -> Accelerate\n"
        #           "LEFT -> Turn Left\nRIGHT -> Turn Right")
            Buf = ""
            # SockTCP.settimeout(2)
        else:
            Window["ButtonLeft"].Update(button_color=("black", "yellow"))
            Window["ButtonUP"].Update(button_color=("black", "yellow"))
            Window["ButtonRight"].Update(button_color=("black", "yellow"))
            # if Key.wait(Key.KEY_UP) or Key.wait("left") or Key.wait("right"):
            if Key.is_pressed(Key.KEY_UP):
                Window["ButtonUP"].Update(button_color=("black", "red"))
                Buf += "2"
            if Key.is_pressed("left"):
                Window["ButtonLeft"].Update(button_color=("black", "red"))
                Buf += "3"
            if Key.is_pressed("right"):
                Window["ButtonRight"].Update(button_color=("black", "red"))
                Buf += "4"
            if Buf == "":
                Buf = "1"
            if Key.is_pressed("c"):
                SockTCP.close()
                exit()
            SockTCP.sendto(bytes(int(Buf)), IP)
            print(Buf)
            Buf = ""
            # time.sleep(0.13)
            timeout = time.time()
            # try:
            SockTCP.recv(8000)
            # except socket.timeout:
            print(time.time() - timeout)
    except socket.timeout:
        continue
    except KeyboardInterrupt:
        GUI.popup_error("Error Occurred while Operation")
        Window.FindElement("Initial").Update("Status : Connection timed out")
        time.sleep(10)
        Window.close()
        SockTCP.close()
        exit(1)
    except Exception:
        GUI.popup_error("Error Occurred while Operation")
        Window.FindElement("Initial").Update("Status : Connection timed out")
        time.sleep(10)
        Window.close()
        SockTCP.close()
        exit(1)

