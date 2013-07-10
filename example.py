from python_hue.hue import Hue
import time

h = Hue(debug=True) # Initialize the class
h.station_ip = "192.168.1.12"  # Your base station IP
h.get_state() # Authenticate, bootstrap your lighting system
l = h.lights.get('l2') # get bulb #3

interval = 3

l.off()
l.on()

l.bri(0)
l.rgb(255,255,255)
l.on()
for slot in range(255):
        l.bri(slot)
        time.sleep(1)

import sys
sys.exit()

# red phase
l.bri(0)
l.rgb(255, 0, 0)
l.on()
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

# l.bri(0) # Dimmest
# l.bri(50) # Brightest
# l.rgb(255, 0, 0) # [0-255 rgb values]
# l.rgb("#FFE303") # Hex string
# l.on()
# l.off()
# l.toggle()
# l.alert() # short alert
# l.alert("lselect") # long alert
# l.setState({"bri": 220, "alert": "select"}) # Complex send
