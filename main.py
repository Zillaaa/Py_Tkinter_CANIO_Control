from tkinter import *
import tkinter as tk
from time import sleep
from random import randint
from pystyle import Colorate, Colors, Box
import serial
import can
from multiprocessing import Process, freeze_support
from time import sleep
from PIL import ImageTk, Image
import cantools
from threading import Thread
from time import sleep

    # buttons 

def sendconfirm1():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0X18EFCC03, data = [0X1,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:            
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:                
                result = db.decode_message(msg.arbitration_id, msg.data)
                tk.Label(scrollable_frame, text=f"BuildDAte").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{result}" )))
                e = False
            else:
                bus.send(nachricht)
                msg = bus.recv(timeout=1)
                r+= 1
                if r > 5:
                    print( "Error while getting response from BuildDAte")
                    tk.Label(scrollable_frame, text="Error: BuildDAte").pack()
                    e = False
    except Exception as e:
        print(Colorate.Horizontal(Colors.red, "Error while sending [BuildDAte]"))
        print(e)

def sendconfirm2():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0X18EFCC03, data = [0X2,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:
            
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:
                tk.Label(scrollable_frame, text=f"BuildTime").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                e = False
            else:
                #bus.send(nachricht)
                r+= 1
                if r > 10:
                    print( "Error while getting response from BuildTime")
                    tk.Label(scrollable_frame, text="Error: BuildTime").pack()
                    e = False
            

    except Exception as e:
        print(Colorate.Horizontal(Colors.red, "Error while sending [BuildTime]"))
        print(e)

def sendconfirm3():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0X18EFCC03, data = [0X3,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:
            
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:
                tk.Label(scrollable_frame, text=f"SerNum").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                e = False
            else:
                #bus.send(nachricht)
                r+= 1
                if r > 10:
                    print( "Error while getting response from SerNum")
                    tk.Label(scrollable_frame, text="Error: SerNum").pack()
                    e = False
            

    except Exception as e:
        print(Colorate.Horizontal(Colors.red, "Error while sending [SerNum]"))
        print(e)

def sendconfirm4():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0X18EFCC03, data = [0X4,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:
            
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:
                tk.Label(scrollable_frame, text=f"SWversion").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                e = False
            else:
                #bus.send(nachricht)
                r+= 1
                if r > 10:
                    print( "Error while getting response from SWversion")
                    tk.Label(scrollable_frame, text="Error: SWversion").pack()
                    e = False
            

    except Exception as e:
        print(Colorate.Horizontal(Colors.red, "Error while sending [SWversion]"))
        print(e)

def sendconfirm5():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0X18EFCC03, data = [0X5,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:
            
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:
                tk.Label(scrollable_frame, text=f"BSPversion").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                e = False
            else:
                #bus.send(nachricht)
                r+= 1
                if r > 10:
                    print( "Error while getting response from BSPversion")
                    tk.Label(scrollable_frame, text="Error: BSPversion").pack()
                    e = False
            

    except Exception as e:
        print(Colorate.Horizontal(Colors.red, "Error while sending [BSPversion]"))
        print(e)

def sendconfirm6():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X10,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:
            #bus.send(nachricht)
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:
                tk.Label(scrollable_frame, text=f"INPUT-AnA").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                e = False
            else:
                r+= 1
                if r > 10:
                    print( "Error while getting response from INPUT-AnA")
                    tk.Label(scrollable_frame, text="Error: INPUT-AnA").pack()
                    e = False
            

    except Exception as e: 
        print(Colorate.Horizontal(Colors.red, "Error while sending [INPUT-AnA]"))
        print(e)

def sendconfirm7():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X11,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:
            #bus.send(nachricht)
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:
                tk.Label(scrollable_frame, text=f"INPUT-AnA-IO").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                e = False
            else:
                r+= 1
                if r > 10:
                    print( "Error while getting response from INPUT-AnA-IO")
                    tk.Label(scrollable_frame, text="Error: INPUT-AnA-IO").pack()
                    e = False
            

    except Exception as e:
        print(Colorate.Horizontal(Colors.red, "Error while sending [INPUT-AnA-IO]"))
        print(e)

def sendconfirm8():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X12,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:
            #bus.send(nachricht)
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:
                tk.Label(scrollable_frame, text=f"Static-AnA-HSD").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                e = False
            else:
                r+= 1
                if r > 10:
                    print( "Error while getting response from Static-AnA-HSD")
                    tk.Label(scrollable_frame, text="Error: Static-AnA-HSD").pack()
                    e = False
            

    except Exception as e:
        print(Colorate.Horizontal(Colors.red, "Error while sending [Static-AnA-HSD]"))
        print(e)

def sendconfirm9():
    global bus
    try:
        e = True
        nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X13,00,00,00,00,00,00], is_extended_id=True)
        bus.send(nachricht)
        r = 0
        while e == True:
            #bus.send(nachricht)
            msg = bus.recv(timeout=1)
            if msg.arbitration_id == 0x18EF03CC:
                tk.Label(scrollable_frame, text=f"Misc").pack()
                print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                e = False
            else:
                r+= 1
                if r > 10:
                    print( "Error while getting response from Misc")
                    tk.Label(scrollable_frame, text="Error: Misc").pack()
                    e = False
            

    except Exception as e:
        print(Colorate.Horizontal(Colors.red, "Error while sending [Misc]"))
        print(e)

def lampe1(shutdown = False):
    global bus
    global l1
    global buttonf10
    if shutdown == True:
        if l1 == True:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X11,00,00,0x18,0xDC,0x00], is_extended_id=True)
            l1 = False
        else:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x11,1,00,0x18,0XDC,0x00], is_extended_id=True)
            l1 = True
        bus.send(nachricht)
        return "Lampe 1 on"
    else:
        try:
            e = True
            if l1 == True:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X11,00,00,0x18,0xDC,0x00], is_extended_id=True)
                l1 =False
            else:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x11,1,00,0x18,0XDC,0x00], is_extended_id=True)
                l1 = True
            bus.send(nachricht)
            r = 0
            while e == True:
                #bus.send(nachricht)
                msg = bus.recv(timeout=1)
                if msg.arbitration_id == 0x18EF03CC:
                    tk.Label(scrollable_frame, text=f"Lampe 1").pack()
                    print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                    e = False

                else:
                    r+= 1
                    if r > 100:
                        #print( "Error while getting response from Lampe 1")
                        #tk.Label(scrollable_frame, text="Error: Lampe 1").pack()
                        e = False
                

        except Exception as e:
            print(Colorate.Horizontal(Colors.red, "Error while sending [Lampe 1]"))
            print(e)

def lampe2(shutdown = False):
    global bus
    global l2
    global buttonf11
    if shutdown == True:
        if l2 == True:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X12,00,00,0x18,0xDC,0x00], is_extended_id=True)
            l2 = False

        else:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x12,1,00,0x18,0XDC,0x00], is_extended_id=True)
            l2 = True
        bus.send(nachricht)
        return "Lampe 2 on"
    else:
        try:
            e = True
            if l2 == True:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X12,00,00,0x18,0xDC,0x00], is_extended_id=True)
                l2 = False
            else:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x12,1,00,0x18,0XDC,0x00], is_extended_id=True)
                l2 = True
            bus.send(nachricht)
            r = 0
            while e == True:
                #bus.send(nachricht)
                msg = bus.recv(timeout=1)
                if msg.arbitration_id == 0x18EF03CC:
                    tk.Label(scrollable_frame, text=f"Lampe 2").pack()
                    print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                    e = False
                else:
                    r+= 1
                    if r > 100:
                        #print( "Error while getting response from Lampe 2")
                        tk.Label(scrollable_frame, text="Error: Lampe 2").pack()
                        e = False
                

        except Exception as e:
            print(Colorate.Horizontal(Colors.red, "Error while sending [Lampe 2]"))
            print(e)

def lampe3(shutdown = False):
    global bus
    global l3
    global buttonf12
    if shutdown == True:
        if l3 == True:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X13,00,00,0x18,0xDC,0x00], is_extended_id=True)
            l3 = False
        else:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x13,1,00,0x18,0XDC,0x00], is_extended_id=True)
            l3 = True
        bus.send(nachricht)
        return "Lampe 3 on"
    else:
        try:
            e = True
            if l3 == True:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X13,00,00,0x18,0xDC,0x00], is_extended_id=True)
                l3 = False
            else:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x13,1,00,0x18,0XDC,0x00], is_extended_id=True)
                l3 = True
            bus.send(nachricht)
            r = 0
            while e == True:
                #bus.send(nachricht)
                msg = bus.recv(timeout=1)
                if msg.arbitration_id == 0x18EF03CC:
                    tk.Label(scrollable_frame, text=f"Lampe 3").pack()
                    print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                    e = False
                else:
                    r+= 1
                    if r > 100:
                        #print( "Error while getting response from Lampe 3")
                        tk.Label(scrollable_frame, text="Error: Lampe 3").pack()
                        e = False
                

        except Exception as e:
            print(Colorate.Horizontal(Colors.red, "Error while sending [Lampe 2]"))
            print(e)

def lampe4(shutdown = False):
    global bus
    global l4
    global buttonf13
    if shutdown == True:
        if l4 == True:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X14,00,00,0x18,0xDC,0x00], is_extended_id=True)
            l4 = False

        else:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x14,1,00,0x18,0XDC,0x00], is_extended_id=True)
            l4 = True
        bus.send(nachricht)
        return "Lampe 4 on"
    else:
        try:
            e = True
            if l4 == True:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X14,00,00,0x18,0xDC,0x00], is_extended_id=True)
                l4 = False
            else:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x14,1,00,0x18,0XDC,0x00], is_extended_id=True)
                l4 = True

            bus.send(nachricht)
            r = 0
            while e == True:
                #bus.send(nachricht)
                msg = bus.recv(timeout=1)
                if msg.arbitration_id == 0x18EF03CC:
                    tk.Label(scrollable_frame, text=f"Lampe 4").pack()
                    print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                    e = False
                else:
                    r+= 1
                    if r > 100:
                        #print( "Error while getting response from Lampe 4")
                        tk.Label(scrollable_frame, text="Error: Lampe 4").pack()
                        e = False
                

        except Exception as e:
            print(Colorate.Horizontal(Colors.red, "Error while sending [Lampe 4]"))
            print(e)

def lampe5(shutdown = False):
    global bus
    global l5
    global buttonf14
    if shutdown == True:
        if l5 == True:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X15,00,00,0x18,0xDC,0x00], is_extended_id=True)
            l5 = False
        else:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x15,1,00,0x18,0XDC,0x00], is_extended_id=True)
            l5 = True
        bus.send(nachricht)
        return "Lampe 5 on"
    else:
        try:
            e = True
            if l5 == True:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X15,00,00,0x18,0xDC,0x00], is_extended_id=True)
                l5 = False

            else:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x15,1,00,0x18,0XDC,0x00], is_extended_id=True)
                l5 = True
            bus.send(nachricht)
            r = 0
            while e == True:
                #bus.send(nachricht)
                msg = bus.recv(timeout=1)
                if msg.arbitration_id == 0x18EF03CC:
                    tk.Label(scrollable_frame, text=f"Lampe 5").pack()
                    print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                    e = False
                else:
                    r+= 1
                    if r > 100:
                        #print( "Error while getting response from Lampe 5")
                        tk.Label(scrollable_frame, text="Error: Lampe 5").pack()
                        e = False
                

        except Exception as e:
            print(Colorate.Horizontal(Colors.red, "Error while sending [Lampe 5]"))
            print(e)

def lampe6(shutdown = False):
    global bus
    global l6
    global buttonf15
    if shutdown == True:
        if l6 == True:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X16,00,00,0x18,0xDC,0x00], is_extended_id=True)
            l6 = False
        else:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x16,1,00,0x18,0XDC,0x00], is_extended_id=True)
            l6 = True
        bus.send(nachricht)
        return "Lampe 6 on"
    else:
        try:
            e = True
            if l6 == True:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X16,00,00,0x18,0xDC,0x00], is_extended_id=True)
                l6 = False

            else:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x16,1,00,0x18,0XDC,0x00], is_extended_id=True)
                l6 = True

            bus.send(nachricht)
            r = 0
            while e == True:
                #bus.send(nachricht)
                msg = bus.recv(timeout=1)
                if msg.arbitration_id == 0x18EF03CC:
                    tk.Label(scrollable_frame, text=f"Lampe 6").pack()
                    print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                    e = False
                else:
                    r+= 1
                    if r > 100:
                        #print( "Error while getting response from Lampe 6")
                        tk.Label(scrollable_frame, text="Error: Lampe 6").pack()
                        e = False
                

        except Exception as e:
            print(Colorate.Horizontal(Colors.red, "Error while sending [Lampe 6]"))
            print(e)

def lampe7(shutdown = False):
    global bus
    global l7
    global buttonf16
    if shutdown == True:
        if l7 == True:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X17,00,00,0x18,0xDC,0x00], is_extended_id=True)
            l7 = False
        else:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x17,1,00,0x18,0XDC,0x00], is_extended_id=True)
            l7 = True
        bus.send(nachricht)
        return "Lampe 7 on"
    else:
        try:
            e = True
            if l7 == True:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X17,00,00,0x18,0xDC,0x00], is_extended_id=True)
                l7 = False

            else:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x17,1,00,0x18,0XDC,0x00], is_extended_id=True)
                l7 = True

            bus.send(nachricht)
            r = 0
            while e == True:
                #bus.send(nachricht)
                msg = bus.recv(timeout=1)
                if msg.arbitration_id == 0x18EF03CC:
                    tk.Label(scrollable_frame, text=f"Lampe 7").pack()
                    print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                    e = False
                else:
                    r+= 1
                    if r > 100:
                        #print( "Error while getting response from Lampe 7")
                        tk.Label(scrollable_frame, text="Error: Lampe 7").pack()
                        e = False
                

        except Exception as e:
            print(Colorate.Horizontal(Colors.red, "Error while sending [Lampe 7]"))
            print(e)

def lampe8(shutdown = False):
    global bus
    global l8
    global buttonf17
    if shutdown == True:
        if l8 == True:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X18,00,00,0x18,0xDC,0x00], is_extended_id=True)
            l8 = False
        else:
            nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x18,1,00,0x18,0XDC,0x00], is_extended_id=True)
            l8 = True

        bus.send(nachricht)
        return "Lampe 8 on"
    else:
        try:
            e = True
            if l8 == True:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0X18,00,00,0x18,0xDC,0x00], is_extended_id=True)
                l8 = False

            else:
                nachricht = can.Message(arbitration_id = 0x18EFCC03, data = [0X20,0x18,1,00,0x18,0XDC,0x00], is_extended_id=True)
                l8 = True

            bus.send(nachricht)
            r = 0
            while e == True:
                #bus.send(nachricht)
                msg = bus.recv(timeout=1)
                if msg.arbitration_id == 0x18EF03CC:
                    tk.Label(scrollable_frame, text=f"Lampe 8").pack()
                    print(Colorate.Horizontal(Colors.cyan_to_green, Box.SimpleCube(f"{msg} || Attempt: {r}" )))
                    e = False
                else:
                    r+= 1
                    if r > 100:
                        #print( "Error while getting response from Lampe 8")
                        tk.Label(scrollable_frame, text="Error: Lampe 8").pack()
                        e = False
                

        except Exception as e:
            print(Colorate.Horizontal(Colors.red, "Error while sending [Lampe 8]"))
            print(e)

def off():
    global l1, l2, l3, l4, l5, l6, l7 ,l8
    l1 = True
    l2 = True
    l3 = True
    l4 = True
    l5 = True
    l6 = True
    l7 = True
    l8 = True

    lampe1()
    lampe2()
    lampe3()
    lampe4()
    lampe5()
    lampe6()
    lampe7()
    lampe8()

    print(Box.Lines("All Lamps are OFF!"))
    
def on():

    global l1, l2, l3, l4, l5, l6, l7 ,l8
    l1 = False
    l2 = False
    l3 = False
    l4 = False
    l5 = False
    l6 = False
    l7 = False
    l8 = False

    lampe1()
    lampe2()
    lampe3()
    lampe4()
    lampe5()
    lampe6()
    lampe7()
    lampe8()

    print(Box.Lines("All Lamps are On!"))

def animation():
    for i in range(20):
        restart()
    print("Done!")

def restart():
    off()
    on()




if __name__ == '__main__':

    freeze_support()



    #db = cantools.database.load_file(r"caniomodule.sym")
    

    l1 = True
    l2 = True
    l3 = True
    l4 = True
    l5 = True
    l6 = True
    l7 = True
    l8 = True


    interface = 'pcan'
    channel = 'PCAN_USBBUS1'
    bitrate = 250000
    try:
        bus = can.interface.Bus(bustype=interface, channel=channel, bitrate=bitrate) 
    except Exception as e:
        print(f"Erro while setting up the Interface! [{e}]")




    root = tk.Tk()
    root.geometry("720x500")
    root.iconbitmap('pictures\AtlasLogo.ico')
    root.title("Controller")




    Lightframe = LabelFrame(root, text="Light Controll")
    Lightframe.place(x=0, y=0)

    Buttonframe = LabelFrame(root, text="Main Controller")
    Buttonframe.place(x=100, y=0)

    buttonf1 = tk.Button(Buttonframe, text="     BuildDAte     ", command=sendconfirm1, bg="green")
    buttonf1.pack()

    buttonf2 = tk.Button(Buttonframe, text="     BuildTime     ", command=sendconfirm2, bg="green")
    buttonf2.pack()

    buttonf3 = tk.Button(Buttonframe, text="       SerNum       ", command=sendconfirm3, bg="green")
    buttonf3.pack()

    buttonf4 = tk.Button(Buttonframe, text="     SWversion     ", command=sendconfirm4, bg="green")
    buttonf4.pack()

    buttonf5 = tk.Button(Buttonframe, text="     BSPversion    ", command=sendconfirm5, bg="green")
    buttonf5.pack()

    buttonf6 = tk.Button(Buttonframe, text="    INPUT-AnA    ", command=sendconfirm6, bg="green")
    buttonf6.pack()

    buttonf7 = tk.Button(Buttonframe, text="  INPUT-AnA-IO ", command=sendconfirm7, bg="green")
    buttonf7.pack()

    buttonf8 = tk.Button(Buttonframe, text="Static-AnA-HSD", command=sendconfirm8, bg="green")
    buttonf8.pack()

    buttonf9 = tk.Button(Buttonframe, text="          Misc          ", command=sendconfirm9, bg="green")
    buttonf9.pack()

    #Lampen####
    buttonf10 = tk.Button(Lightframe, text="Lampe 1", command=lampe1, bg="yellow")
    buttonf10.pack()

    buttonf11 = tk.Button(Lightframe, text="Lampe 2", command=lampe2, bg="yellow")
    buttonf11.pack()

    buttonf12 = tk.Button(Lightframe, text="Lampe 3", command=lampe3, bg="yellow")
    buttonf12.pack()

    buttonf13 = tk.Button(Lightframe, text="Lampe 4", command=lampe4, bg="yellow")
    buttonf13.pack()

    buttonf14 = tk.Button(Lightframe, text="Lampe 5", command=lampe5, bg="yellow")
    buttonf14.pack()

    buttonf15 = tk.Button(Lightframe, text="Lampe 6", command=lampe6, bg="yellow")
    buttonf15.pack()

    buttonf16 = tk.Button(Lightframe, text="Lampe 7", command=lampe7, bg="yellow")
    buttonf16.pack()

    buttonf17 = tk.Button(Lightframe, text="Lampe 8", command=lampe8, bg="yellow")
    buttonf17.pack()

    ##on off
    ONOFFframe = LabelFrame(Lightframe, text="Main Controll")
    ONOFFframe.pack()
    offButton = tk.Button(ONOFFframe, text="All Off", command=off, bg="red")
    offButton.pack()

    onButton = tk.Button(ONOFFframe, text="All On", command=on, bg="green")
    onButton.pack()

    restartButton = tk.Button(ONOFFframe, text="Reconnect", command=restart, bg="orange")
    

    aniButton = tk.Button(ONOFFframe, text="Animation", command=animation, bg="grey")
    aniButton.pack()
    restartButton.pack()

    ##UI
    
    logoFrame = Frame(root, width=200, height=200)
    logoFrame.place(x=620, y=0)

    OPframe = LabelFrame(root, text="Light Controll")
    OPframe.place(x=0, y=0)

    logo = ImageTk.PhotoImage(Image.open("pictures\AtlasLogo_50dpi.png"))

    logoLabel = Label(logoFrame, image= logo)
    logoLabel.pack()

    #scroll Output
    container = tk.LabelFrame(root, text="Output")
    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(  
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    tk.Label(scrollable_frame).pack()

    container.place(x=210, y=0)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()
    ###off###
    l1 = False
    l2 = False
    l3 = False
    l4 = False
    l5 = False
    l6 = False
    l7 = False
    l8 = False

    print(lampe1(True))
    print(lampe2(True))
    print(lampe3(True))
    print(lampe4(True))
    print(lampe5(True))
    print(lampe6(True))
    print(lampe7(True))
    print(lampe8(True))

    print(Colorate.Horizontal(Colors.red_to_purple,"|--Closed--|"))  