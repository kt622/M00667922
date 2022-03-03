import opc
import time
import random
import colorsys


leds = [(0,0,0)]*360
led = 0
id = []

All = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359]
Blue = [3, 63, 123,183,243,303,304,305,306,246,247,186,187,124,125,66,67,6,5,4,9,69,129,189,249,309,310,311,312,313,15,75,135,195,255,315,316,317,318,319,320,260,200,140,80,20,22,23,24,25,82,142,143,144,145,202,262,322,323,324,325]
Red = [3,4,63,64,123,124,183,184,243,244,303,304,5,6,7,8,9,10,69,70,128,127,126,125,186,187,247,248,308,309,14,15,16,17,18,19,20,74,75,76,77,78,79,80,134,135,194,195,196,197,198,199,200,254,255,314,315,316,317,318,319,320,25,85,26,86,145,146,205,206,265,266,325,326,27,28,29,30,87,88,89,90,91,92,151,152,153,211,212,213,271,270,330,269,329,268,328,329,267,327]
Green = [2,3,62,63,122,123,182,183,242,243,302,303,4,5,6,7,8,9,67,68,69,304,305,306,307,308,309,249,248,189,188,187,186,12,13,72,73,132,133,192,193,252,253,312,313,14,74,15,75,16,76,17,77,78,138,198,197,196,195,194,256,257,317,318,21,81,22,82,23,83,24,84,25,85,26,86,27,87,141,142,201,202,203,204,205,206,207,261,262,321,322,323,324,325,326,327,30,90,31,91,32,92,33,93,34,94,35,95,36,96,150,151,210,211,212,213,214,215,216,270,271,330,331,332,333,334,335,336,339,340,279,280,219,220,159,160,99,100,39,40,41,101,42,102,162,163,222,223,283,284,343,344,345,346,285,286,225,226,165,166,105,106,45,46]

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

colourBlue = (0,0,225)
colourRed = (255,0,0)
colourGreen = (0,255,0)

s = 1.0 #max colour
v = 1.0 #max bightness

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

#-------------------------------------------------------------

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


