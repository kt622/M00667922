#senary code
import opc
import time
import random
import colorsys
import tkinter as tk
from tkinter import *
from tkinter import ttk

leds = [(0,0,0)]*360 #black
led = 0
window = Tk()

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#-------------------Lists--------------------------------#

Transition = [30,90,150,210,270,330,29,89,149,209,269,329]
RightCurtains = [30,90,150,210,270,330]
LeftCurtains = [29,89,149,209,269,329]
FBuilding = [303,304,243,244,306,307,308,246,247,248,186,187,188,126,127,128,314,315,254,255,194,195,134,135,322,323,254,255,194,195,134,135,322,323,324,262,263,264,202,203,204,322,314,262,263,264,202,204,326,327,328,266,267,268,330,331,270,271,210,211,150,151,338,339,278,279,342,343,344,345,282,283,284,285,222,223,224,225,348,349,350,351,288,289,290,291,228,229,230,231,355,356,357,295,296,297,235,236,237,175,176,177,115,116,117]
#MBuilding = [309,310,249,250,189,190,121,318,319,320,258,259,260,198,199,200,325,265,205,145,144,143,334,335,336,274,275,276,340,341,280,281,162,163,102,103,352,292,232,172,171,170]
BBuilding = [309,310,249,250,189,190,129,130,318,319,320,258,259,260,198,199,200,325,265,205,145,144,143,334,335,336,274,275,276,340,341,280,281,162,163,102,103,352,292,232,172,171,170, 301,302,241,242,181,182,183,121,122,123,305,245,185,68,69,70,311,313,251,252,253,316,317,256,257,321,261,201,141,142,81,82,329,269,209,332,333,272,273,337,277,341,281,164,165,346,347,286,287,353,354,293,294,233,234]
Circle = [36, 37, 95, 96, 97, 98, 156, 157]
StarsL = [33,57,2,39,6,12,29,27,19,15,22,111,105,86,73,64,65,78,84,100,109,167,173,178,131,120,137,148,214,206,226,239]
#TS = [2,5,6,12,15,22,19,27,29,39,42,57,33]
All = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359]
Blue = [3, 63, 123,183,243,303,304,305,306,246,247,186,187,124,125,66,67,6,5,4,9,69,129,189,249,309,310,311,312,313,15,75,135,195,255,315,316,317,318,319,320,260,200,140,80,20,22,23,24,25,82,142,143,144,145,202,262,322,323,324,325]
Red = [3,4,63,64,123,124,183,184,243,244,303,304,5,6,7,8,9,10,69,70,128,127,126,125,186,187,247,248,308,309,14,15,16,17,18,19,20,74,75,76,77,78,79,80,134,135,194,195,196,197,198,199,200,254,255,314,315,316,317,318,319,320,25,85,26,86,145,146,205,206,265,266,325,326,27,28,29,30,87,88,89,90,91,92,151,152,153,211,212,213,271,270,330,269,329,268,328,329,267,327]
Green = [2,3,62,63,122,123,182,183,242,243,302,303,4,5,6,7,8,9,67,68,69,304,305,306,307,308,309,249,248,189,188,187,186,12,13,72,73,132,133,192,193,252,253,312,313,14,74,15,75,16,76,17,77,78,138,198,197,196,195,194,256,257,317,318,21,81,22,82,23,83,24,84,25,85,26,86,27,87,141,142,201,202,203,204,205,206,207,261,262,321,322,323,324,325,326,327,30,90,31,91,32,92,33,93,34,94,35,95,36,96,150,151,210,211,212,213,214,215,216,270,271,330,331,332,333,334,335,336,339,340,279,280,219,220,159,160,99,100,39,40,41,101,42,102,162,163,222,223,283,284,343,344,345,346,285,286,225,226,165,166,105,106,45,46]

#------------------SomeDefinedColours------------------#
ColourW = (225,225,153)
ColourB = (54,69,79)
ColourG1 = (180,180,180)
ColourG2 = (100,100,100)
colourBlue = (0,0,225)
colourRed = (255,0,0)
colourGreen = (0,255,0)

#----------------Definitions---------------------------#
#RGB Colour def
def colour(colour):
    for led in All:
        leds[led] = (colour)
        time.sleep(0.0000000000000001)
        client.put_pixels(leds)
        
def clear():
    for led in All:
        leds[led] = (0,0,0)
        time.sleep(0.0000000000000001)
        client.put_pixels(leds)

def blue(colour):
    for led in Blue:
        leds[led] = colour
        #time.sleep(0.02)
        client.put_pixels(leds)

def red(colour):    
    for led in Red:
        leds[led] = colour
        #time.sleep(0.02)
        client.put_pixels(leds)
        
def green(colour):
    for led in Green:
        leds[led] = colour
        #time.sleep(0.02)
        client.put_pixels(leds)


#Views
def FrontB ():
    for led in FBuilding:
        leds[led] = ColourG1
        time.sleep(0.02)
        client.put_pixels(leds)


def BackB ():
    for led in BBuilding:
        leds[led] = ColourB
        time.sleep(0.02)
        client.put_pixels(leds)
    

def Moon ():
    for led in Circle:
        leds[led] = (ColourW)
        time.sleep(0.02)
        client.put_pixels(leds)

def Sun ():
    for led in Circle:
        leds[10+led-1] = (255,50,0)
        #time.sleep(0.2)
        client.put_pixels(leds)

def Stars ():
    for led in StarsL:
        leds[led] = (255,255,153)
        time.sleep(0.1)
        client.put_pixels(leds)

        
def Twinkle():
    while True: 
        for led in StarsL:
            leds[led] = (225,225,153)
        time.sleep(.2)
        client.put_pixels(leds)
        for led in StarsL:
            leds[led] = (0,0,0)
        time.sleep(.2)
        client.put_pixels(leds)
        break


def BlinkStars(TS):
    #while True:
        if led in Stars == 59:
            leds [2] = (225,225,153)
            time.sleep(1)
            client.put_pixels(leds)
            leds[2] = (0,0,0)
            time.sleep(1)
            client.put_pixels(leds)
            
        if led in Stars == 119:
            leds[led-90] = (0,0,0)
            time.sleep(0.1)
            client.put_pixels(leds)
        if led in Stars == 239:
            leds[led-150] = (0,0,0)
            time.sleep(0.1)
            client.put_pixels(leds)
        if led in Stars == 359:
            leds[led-210] = (0,0,0)
            time.sleep(0.1)
            client.put_pixels(leds)
                #time.sleep(5)

def PlaneFly (): #difined plane object flying from left to right of the screen 
    for led in range (45): #range I want the plane to move (distance)
        leds = [(0,0,0)]*360 #All leds black (background)

        leds[225-led] = (200,200,200) #in process of creating objects to transition
        leds[226-led] = (200,200,200)
        leds[167-led] = (200,200,200)
        leds[227-led] = (200,200,200)
        leds[287-led] = (200,200,200)
        leds[108-led] = (200,200,200)
        leds[168-led] = (200,200,200)
        leds[228-led] = (200,200,200)
        leds[288-led] = (200,200,200)
        leds[349-led] = (200,200,200)
        leds[348-led] = (200,200,200)
        leds[109-led] = (200,200,200)
        leds[169-led] = (255,0,0)
        leds[229-led] = (200,200,200)
        leds[289-led] = (225,0,0)
        leds[349-led] = (200,200,200)
        leds[230-led] = (200,200,200)
        leds[231-led] = (200,200,200)
        leds[232-led] = (200,200,200)
        leds[233-led] = (200,200,200)
        leds[173-led] = (200,200,200)
        leds[293-led] = (200,200,200)
        leds[234-led] = (200,200,200)
        client.put_pixels(leds)
        time.sleep(.4)

def Boat():
    for led in range (43):
        leds = [(0,0,0)]*360
        #boat
        leds[265-led+18] = (165,42,42) #Brown colour
        leds[266-led+18] = (165,42,42)
        leds[267-led+18] = (165,42,42)
        leds[268-led+18] = (165,42,42)
        leds[269-led+18] = (165,42,42)
        leds[270-led+18] = (165,42,42)
        leds[271-led+18] = (165,42,42)
        leds[272-led+18] = (165,42,42)
        leds[273-led+18] = (165,42,42)
        leds[274-led+18] = (165,42,42)
        leds[326-led+18] = (165,42,42)
        leds[327-led+18] = (165,42,42)
        leds[328-led+18] = (165,42,42)
        leds[329-led+18] = (165,42,42)
        leds[330-led+18] = (165,42,42)
        leds[331-led+18] = (165,42,42)
        leds[332-led+18] = (165,42,42)
        leds[333-led+18] = (165,42,42)
        #sail
        leds[209-led+18] = (80,80,80) #Grey colour
        leds[149-led+18] = (80,80,80)
        leds[89-led+18] = (80,80,80)
        leds[90-led+18] = (50,50,50) #Dark grey colour
        leds[150-led+18] = (50,50,50)
        leds[91-led+18] = (225,0,0) #Red colour
        leds[92-led+18] = (225,0,0)
        leds[151-led+18] = (225,0,0)
        leds[152-led+18] = (225,0,0)
        leds[153-led+18] = (225,0,0)
        client.put_pixels(leds)
        time.sleep(.1)
        
    

def Ghost(): #defined ghost object traveling from 
    for led in range (48):
        leds = [(0,0,0)]*360
        #ghost
        leds[80-30-led] = (255,255,255)
        leds[81-30-led] = (255,255,255)
        leds[82-30-led] = (255,255,255)
        leds[138-30-led] = (255,255,255)
        leds[139-30-led] = (255,0,255)
        leds[140-30-led] = (255,0,255)
        leds[141-30-led] = (255,255,255)
        leds[142-30-led] = (255,0,255)
        leds[143-30-led] = (255,0,255)
        leds[144-30-led] = (255,255,255)
        leds[197-30-led] = (255,255,255)
        leds[198-30-led] = (255,255,255)
        leds[199-30-led] = (255,0,255)
        leds[200-30-led] = (255,0,255)
        
        leds[201-30-led] = (255,255,255)
        leds[202-30-led] = (255,0,255)
        leds[203-30-led] = (255,0,255)
        leds[204-30-led] = (255,255,255)
        leds[205-30-led] = (255,255,255)
        leds[257-30-led] = (255,255,255)
        leds[258-30-led] = (255,255,255)
        leds[259-30-led] = (255,255,255)
        leds[260-30-led] = (255,255,255)
        leds[261-30-led] = (255,255,255)
        leds[262-30-led] = (255,255,255)
        leds[263-30-led] = (255,255,255)
        leds[264-30-led] = (255,255,255)
        leds[317-30-led] = (255,255,255)
        leds[318-30-led] = (255,255,255)
        leds[320-30-led] = (255,255,255)
        leds[322-30-led] = (255,255,255)
        leds[324-30-led] = (255,255,255)
        leds[325-30-led] = (255,255,255)
        client.put_pixels(leds)
        time.sleep(.1)
    #if led in ManMove >= Transition:
        #leds[led] = leds
        #client.put_pixels(leds)
        #time.sleep(.1)

def Drift():
    for led in Transition:
        leds[led] = (225,225,225)
        #time.sleep(0.8)
        client.put_pixels(leds)

def Cutrains (): #transition curtains
    for led in Transition:
        leds[led] = (0,0,0)
        client.put_pixels(leds)


        for led in range (30):
            if led in Transition == 59:
                leds[led] = (0,0,0)
                #time.sleep(0.1)
                client.put_pixels(leds)
            if led in Transition == 119:
                leds[led-90] = (0,0,0)
                #time.sleep(0.1)
                client.put_pixels(leds)
            if led in Transition == 239:
                leds[led-150] = (0,0,0)
                #time.sleep(0.1)
                client.put_pixels(leds)
            if led in Transition == 359:
                leds[led-210] = (0,0,0)
                #time.sleep(0.1)
                client.put_pixels(leds)
            
        #else:
        for led in range (30):
                leds[led-30] = ColourG2
                leds[led-90] = ColourG2
                leds[led-150] = ColourG2
                leds[led-210] = ColourG2
                leds[led-270] = ColourG2
                leds[led-330] = ColourG2
                leds[29-led] = ColourG2
                leds[89-led] = ColourG2
                leds[149-led] = ColourG2
                leds[209-led] = ColourG2
                leds[269-led] = ColourG2
                leds[329-led] = ColourG2
                time.sleep(.1)
                client.put_pixels(leds)

s = 1.0 #max colour
v = 1.0 #max bightness
StartOfHue = 219 #value of colour

def Sea():
    for led in range(180,360,1):
        leds[led] = (0,0,255)
    client.put_pixels(leds)
    time.sleep(.01)
    for x in range(2):
        for hue in range (180,360,1): #for 
            rgb_fraction = colorsys.hsv_to_rgb(hue/13.0, s, v)
            r = rgb_fraction[2] #extract said floating point numbers
            g = rgb_fraction[1]
            b = rgb_fraction[0]

            rgb = (r, g, b*255)
            leds[hue] = rgb
            client.put_pixels(leds)
            time.sleep(.05)
        for led in range(180,360,1):
            leds[led] = (0,0,255)
        client.put_pixels(leds)
        time.sleep(.01)
            
            
def Sand():
    for led in range (120,180,1):
        leds[led] = (152,118,84)
    client.put_pixels(leds)
    time.sleep(.01)

def Sand2Sun():
    for led in range(120,180,1):
        leds[led] = (0,0,0)
    client.put_pixels(leds)
    time.sleep(.01)
                     
    Sun()
    for led in range (180,240,1):
        leds[led] = (152,118,84)
    client.put_pixels(leds)
    time.sleep(.01)

def Cloud():
    for x in range(3):
        for led in range(6,13,1):
            leds[led] = (225,225,225)
        client.put_pixels(leds)
        for led in range(65,74,1):
            leds[led] = (225,225,225)
        client.put_pixels(leds)
        for led in range(126,133,1):
            leds[led] = (225,225,225)
        client.put_pixels(leds)


def Rainbow ():
    for x in range (0,360,1): #for 
            rgb_fraction = colorsys.hsv_to_rgb(x/360.0, s, v)
            r = rgb_fraction[0] #extract said floating point numbers
            g = rgb_fraction[1]
            b = rgb_fraction[2]

            rgb = (r*255, g*255, b*255)
            leds[x] = rgb
            client.put_pixels(leds)
            time.sleep(.01)            

        



    #for hue in range (
        
##        leds[led] = (0,0,255)
##
##        r,g,b = led in range (300,360,1)
##        leds[led] = (0,0,255)
##        while b > 0:
##            b += 5
##        new_val = (r,g,b)
##        leds[led] = new_val
##        #client.put_pixels(leds)
##        #while True:
##        for pixles in range (4):
##            for x in range(300,360):
##                rgb_fraction = colorsys.hsv_to_rgb(((StartOfHue+x))/25.0, s, x/60) #colorsys returns floats between 0 and 1
##                r,g,b = rgb_fraction #extract floating point numbers while converting to rgb range
##                leds[x] = (r*0,g*0,b*255)
##        client.put_pixels(leds)
##        time.sleep(0.3)
##        break

#def for rbg to run all at once
def RGBcolours():
    clear()
    red(colourRed)
    time.sleep(3)
    clear()
    colour(colourRed)
    clear()
    green(colourGreen)
    time.sleep(3)
    clear()
    colour(colourGreen)
    clear()
    blue(colourBlue)
    time.sleep(3)
    clear()
    colour(colourBlue)
    clear()
    Rainbow()
    info = Label(window, text = "RGB means, Red, Green, Blue! All together it makes a rainbow!").grid(row = 5, column = 0)

def FlyingtoCity():
    PlaneFly()
    Moon ()
    FrontB ()
    BackB ()
    Stars()
    Twinkle()
    Twinkle()
    Twinkle()
    Twinkle()
    Stars()
    info1 = Label(window, text = "You arrived at a city, it's nighttime but look at that view!").grid(row = 5, column = 0)

def SailingtoBeach():
    Boat()
    Sun()
    Sand()
    Sea()
    Sand2Sun()
    Cloud()
    Sun()
    info2 = Label(window, text = "You sailed by a beach! It's a shame there's no sunset").grid(row = 5, column = 0)
    

#-----------------------CallingFunctions-------------------#

#Rainbow()
#time.sleep(5)
##red(colourRed)
##time.sleep(3)
##clear()
##colour(colourRed)
##clear()
##green(colourGreen)
##time.sleep(3)
##clear()
##colour(colourGreen)
##clear()
##blue(colourBlue)
##time.sleep(3)
##clear()
##colour(colourBlue)
##clear()
#Rainbow()
#time.sleep(5)
#PlaneFly()

        
##Moon ()
##FrontB ()
##BackB ()
##Stars()
##Twinkle()
##Twinkle()
##Twinkle()
##Twinkle()


##PlaneFly()
##Drift()
##Curtains()
##Boat()
##Beach()

#Sea()
#Sun()

#-----------------------------WindowBox------------------#
window.title('Animation Window')

User = Label(window, text = "Click Button").grid(row = 1, column = 0)

def ColourWord():
    import Ani1

def ColourShow():
    import Ani2


#ColourWord = Button(window, text = "R,G,B", command = ColourWord).grid(row = 2, column = 0)
#ColourShow = Button(window, text = "Colour Show", command = ColourShow).grid(row = 3, column = 0)

#assigning buttons
Guide = Label(window, text = "Click below to: ", width = 40, height = 2).grid(row = 1, column = 0)

Button1 = Button(window, text = "See RGB Colours", command = RGBcolours).grid(row = 2, column = 0)

Button2 = Button(window, text = "Trave by Plane?", command = FlyingtoCity).grid(row = 3, column = 0)

Button2 = Button(window, text = "Trave by Boat?", command = SailingtoBeach).grid(row = 4, column = 0)

Button3 = Button(window, text = "Something Spookie?").grid(row = 5, column = 0)

window.mainloop()

