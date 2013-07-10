from python_hue.hue import Hue
import time

h = Hue() # Initialize the class
h.station_ip = "192.168.1.12"  # Your base station IP
h.get_state() # Authenticate, bootstrap your lighting system
l = h.lights.get('l3') # get bulb #3

interval = 3

import sys
sys.exit()

l.off()

# red phase
l.bri(0)
l.on()
l.rgb(255, 0, 0)
for slot in range(175):
	l.bri(slot)
	time.sleep(interval)

# orange phase
l.bri(150)
l.rgb(255, 75, 0)
for slot in range(150, 200):
	l.bri(slot)
	time.sleep(interval)

# white phase
l.bri(150)
l.rgb(255, 255, 255)
for slot in range(175, 250):
	l.bri(slot)
	time.sleep(interval)
