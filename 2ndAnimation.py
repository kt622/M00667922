###chase and catch code
##import opc
##import time
##import random
##
##leds = [(0,0,0)]*360
##
##client = opc.Client('localhost:7890')
##client.put_pixels(leds)
##client.put_pixels(leds)
##
##led = 0
##while led<59:
##    for led in range (45): #(59):
##        leds = [(0,0,0)]*360
####        leds[20-led] = (255,255,255)
####        leds[21-led] = (255,255,255)
####        leds[22-led] = (255,255,255)
##        leds[80-30-led] = (255,255,255)
##        leds[81-30-led] = (255,255,255)
##        leds[82-30-led] = (255,255,255)
##        leds[138-30-led] = (255,255,255)
##        leds[139-30-led] = (255,0,255)
##        leds[140-30-led] = (255,0,255)
##        leds[141-30-led] = (255,255,255)
##        leds[142-30-led] = (255,0,255)
##        leds[143-30-led] = (255,0,255)
##        leds[144-30-led] = (255,255,255)
##        leds[197-30-led] = (255,255,255)
##        leds[198-30-led] = (255,255,255)
##        leds[199-30-led] = (255,0,255)
##        leds[200-30-led] = (255,0,255)
##        leds[201-30-led] = (255,255,255)
##        leds[202-30-led] = (255,0,255)
##        leds[203-30-led] = (255,0,255)
##        leds[204-30-led] = (255,255,255)
##        leds[205-30-led] = (255,255,255)
##        leds[257-30-led] = (255,255,255)
##        leds[258-30-led] = (255,255,255)
##        leds[259-30-led] = (255,255,255)
##        leds[260-30-led] = (255,255,255)
##        leds[261-30-led] = (255,255,255)
##        leds[262-30-led] = (255,255,255)
##        leds[263-30-led] = (255,255,255)
##        leds[264-30-led] = (255,255,255)
##        leds[317-30-led] = (255,255,255)
##        leds[318-30-led] = (255,255,255)
##        leds[320-30-led] = (255,255,255)
##        leds[322-30-led] = (255,255,255)
##        leds[324-30-led] = (255,255,255)
##        leds[325-30-led] = (255,255,255)
##        
##        client.put_pixels(leds)
##        time.sleep(.1)
##    break
###chase and catch code

#senary code
import opc
import time
import random
import colorsys


leds = [(30,30,30)]*360 #dark grey
led = 0

FBuilding = [303,304,243,244,306,307,308,246,247,248,186,187,188,126,127,128,314,315,254,255,194,195,134,135,322,323,254,255,194,195,134,135,322,323,324,262,263,264,202,203,204,322,314,262,263,264,202,204,326,327,328,266,267,268,330,331,270,271,210,211,150,151,338,339,278,279,342,343,344,345,282,283,284,285,222,223,224,225,348,349,350,351,288,289,290,291,228,229,230,231,355,356,357,295,296,297,235,236,237,175,176,177,115,116,117]
#MBuilding = [309,310,249,250,189,190,121,318,319,320,258,259,260,198,199,200,325,265,205,145,144,143,334,335,336,274,275,276,340,341,280,281,162,163,102,103,352,292,232,172,171,170]
BBuilding = [309,310,249,250,189,190,121,129,130,318,319,320,258,259,260,198,199,200,325,265,205,145,144,143,334,335,336,274,275,276,340,341,280,281,162,163,102,103,352,292,232,172,171,170, 301,302,241,242,181,182,183,121,122,123,305,245,185,68,69,70,311,313,251,252,253,316,317,256,257,321,261,201,141,142,81,82,329,269,209,332,333,272,273,337,277,341,281,164,165,346,347,286,287,353,354,293,294,233,234]
Moon1 = [36, 37, 95, 96, 97, 98, 156, 157]

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

ColourW = (225,225,225)
ColourB = (54,69,79)
ColourG1 = (211,211,211)
ColourG2 = (128,128,128)


def FrontB ():
    for led in FBuilding:
        leds[led] = ColourG1
        time.sleep(0.02)
        client.put_pixels(leds)

##def MidB ():
##    for led in MBuilding:
##        leds[led] = ColourG2
##        time.sleep(0.02)
##        client.put_pixels(leds)

def BackB ():
    for led in BBuilding:
        leds[led] = ColourB
        time.sleep(0.02)
        client.put_pixels(leds)
    

def Moon ():
    for led in Moon1:
        leds[led] = (ColourW)
        time.sleep(0.02)
        client.put_pixels(leds)


FrontB ()
#MidB ()
BackB ()
Moon ()

##while led < 60: # stary sky in city (moon)
##    if led in range (59):
##        leds = [(255,0,255)]*180
##        time.sleep(1)
##        client.put_pixels(leds)
##        
##        leds [36] = (255,255,255)
##        leds [37] = (255,255,255)
##        leds [95] = (255,255,255)
##        leds [96] = (255,255,255)
##        leds [97] = (255,255,255)
##        leds [98] = (255,255,255)
##        leds [156] = (255,255,255)
##        leds [157] = (255,255,255)
##        client.put_pixels(leds)
##
##    if led in range (119):
##        leds = [(255,0,255)]*180
##        time.sleep(1)
##        client.put_pixels(leds)
##        
##        leds [86] = (0,255,0)
##        leds [100] = (0,0,255)
##        time.sleep(1)
##        client.put_pixels(leds)
#more edits to make for sunset, rain and city
        

##        leds = [(255,0,255)]*5
##        time.sleep(1)
##        client.put_pixels(leds)

#client.put_pixels(led_colour)
#client.put_pixels(led_colour)


##import opc
##
##leds = [(0,0,0)]*360
##led = 0
##
##client = opc.Client('localhost:7890')
##client.put_pixels(leds)
##client.put_pixels(leds)
##
##led_colour=[(225,225,0)]*10
##
##led_colour[5] = (0,225,0)
##
##r,g,b = led_colour[7]
##
##while r > 0:
##    r -= 5
##    b += 5
##new_vals = (r,g,b)
##led_colour[7] = new_vals
##
