import opc
import time
import random

leds = [(0,0,0)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

led = 0
while led<59:
    for led in range (45): #(59):
        leds = [(0,0,0)]*360
##        leds[20-led] = (255,255,255)
##        leds[21-led] = (255,255,255)
##        leds[22-led] = (255,255,255)
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
    break


##import opc
##import time
##import random
##import colorsys
##
##leds = [(255,255,255)]*360
##led = 0
##
##
##client = opc.Client('localhost:7890')
##client.put_pixels(leds)
##client.put_pixels(leds)
##
##while led < 60:
##    for led in range (59):
##        led_colour = [(0,0,0)]*360
##        led_colour [1-led] = (0,225,0)
##        led_colour [1-led+6] = (225,0,225)
##        led_colour [1-led] = (255,225,0)
##        led_colour [1-led+6] = (0,225,255)
##        time.sleep(0.2)
##        client.put_pixels(led_colour)
##    break
##
##
##
##client.put_pixels(led_colour)
##client.put_pixels(led_colour)


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
