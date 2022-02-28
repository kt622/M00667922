#senary code
import opc
import time
##import random
import colorsys


leds = [(0,0,0)]*360 #black
led = 0

Transition = [30,90,150,210,270,330,29,89,149,209,269,329]
RightCurtains = [30,90,150,210,270,330]
LeftCurtains = [29,89,149,209,269,329]
FBuilding = [303,304,243,244,306,307,308,246,247,248,186,187,188,126,127,128,314,315,254,255,194,195,134,135,322,323,254,255,194,195,134,135,322,323,324,262,263,264,202,203,204,322,314,262,263,264,202,204,326,327,328,266,267,268,330,331,270,271,210,211,150,151,338,339,278,279,342,343,344,345,282,283,284,285,222,223,224,225,348,349,350,351,288,289,290,291,228,229,230,231,355,356,357,295,296,297,235,236,237,175,176,177,115,116,117]
#MBuilding = [309,310,249,250,189,190,121,318,319,320,258,259,260,198,199,200,325,265,205,145,144,143,334,335,336,274,275,276,340,341,280,281,162,163,102,103,352,292,232,172,171,170]
BBuilding = [309,310,249,250,189,190,129,130,318,319,320,258,259,260,198,199,200,325,265,205,145,144,143,334,335,336,274,275,276,340,341,280,281,162,163,102,103,352,292,232,172,171,170, 301,302,241,242,181,182,183,121,122,123,305,245,185,68,69,70,311,313,251,252,253,316,317,256,257,321,261,201,141,142,81,82,329,269,209,332,333,272,273,337,277,341,281,164,165,346,347,286,287,353,354,293,294,233,234]
Moon1 = [36, 37, 95, 96, 97, 98, 156, 157]
StarsL = [33,57,2,39,6,12,29,27,19,15,22,111,105,86,73,64,65,78,84,100,109,167,173,178,131,120,137,148,214,206,226,239]
TS = [2,5,6,12,15,22,19,27,29,39,42,57,33]

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

ColourW = (225,225,153)
ColourB = (54,69,79)
ColourG1 = (180,180,180)
ColourG2 = (100,100,100)


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

def Stars ():
    for led in StarsL:
        leds[led] = (255,255,153)
        time.sleep(0.1)
        client.put_pixels(leds)
        

#while led < 360:# blinking stars
def Twinkle():
    while True: #for led in range(360):#range (369):
        for led in StarsL:
            leds[led] = (225,225,153)
        time.sleep(.2)
        client.put_pixels(leds)
        for led in StarsL:
            leds[led] = (0,0,0)
        time.sleep(.2)
        client.put_pixels(leds)
        break
##            leds [2] = (255,255,153) 
##            leds [5] = (255,255,153)
##            leds [6] = (255,255,153)
##            leds [12] = (255,255,153)
##            leds [15] = (255,255,153)
##            leds [22] = (255,255,153)
##            leds [19] = (255,255,153)
##            leds [27] = (255,255,153)
##            leds [29] = (255,255,153)
##            leds [39] = (255,255,153)
##            leds [42] = (255,255,153)
##            leds [57] = (255,255,153)
##            leds [33] = (255,255,153)
##            time.sleep(.2)
##            client.put_pixels(leds)
##
##            leds [64] = (255,255,153) 
##            leds [66] = (255,255,153)
##            leds [73] = (255,255,153)
##            leds [78] = (255,255,153)
##            leds [84] = (255,255,153)
##            leds [86] = (255,255,153)
##            leds [100] = (255,255,153)
##            leds [105] = (255,255,153)
##            leds [109] = (255,255,153)
##            leds [111] = (255,255,153)
##            time.sleep(1)
##            client.put_pixels(leds)
##            
##
##            leds [120] = (255,255,153) 
##            leds [131] = (255,255,153)
##            leds [137] = (255,255,153)
##            leds [148] = (255,255,153)
##            leds [152] = (255,255,153)
##            leds [167] = (255,255,153)
##            leds [173] = (255,255,153)
##            leds [178] = (255,255,153)
##            time.sleep(.8)
##            client.put_pixels(leds)
##                
##            leds [206] = (255,255,153) 
##            leds [214] = (255,255,153)
##            leds [226] = (255,255,153)
##            leds [239] = (255,255,153)
##            time.sleep(.5)
##            client.put_pixels(leds)

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
            
Moon ()
FrontB ()
#MidB ()
BackB ()
Stars()
Twinkle()
Twinkle()
Twinkle()
Twinkle()






##for led in TS:
##    leds[led] = (0,0,0)
##    client.put_pixels(leds)
##        
##    for led in range (360):
##            if led in Transition == 59:
##                leds[led] = (0,0,0)
##                #time.sleep(0.1)
##                client.put_pixels(leds)
##            if led in Transition == 119:
##                leds[led] = (0,0,0)
##                #time.sleep(0.1)
##                client.put_pixels(leds)
##            if led in Transition == 239:
##                leds[led] = (0,0,0)
##                #time.sleep(0.1)
##                client.put_pixels(leds)
##            if led in Transition == 359:
##                leds[led] = (0,0,0)
##                #time.sleep(0.1)
##                client.put_pixels(leds)
##    #break

leds = [(0,0,0)]*360
client.put_pixels(leds)
client.put_pixels(leds)


#travel code
def PlaneFly ():
    for led in range (48): #(59):
        leds = [(0,0,0)]*360
##        leds[20-led] = (255,255,255)
##        leds[21-led] = (255,255,255)
##        leds[22-led] = (255,255,255)
        leds[225-led] = 200,200,200) #in process of creating objects to transition
        leds[226-led]
        leds[167-led]
        leds[227-led]
        leds[287-led]
        
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

def Move (): #transition curtains
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

                
        

##                leds[59-led] = ColourW
##                leds[119-led] = ColourW
##                leds[179-led] = ColourW
##                leds[239-led] = ColourG1
##                leds[299-led] = ColourW
##                leds[359-led] = ColourG1
        #return current
        
        client.put_pixels(leds)
        time.sleep(.1)

ManMove()
Drift()
Move()


#travel code


leds = [(0,0,0)]*360
led = 0

#client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led_colour=[(225,225,0)]*10

led_colour[5] = (0,225,0)

r,g,b = led_colour[7]

while r > 0:
    r -= 5
    b += 5
new_vals = (r,g,b)
led_colour[7] = new_vals

