from python_hue.hue import Hue

h = Hue() # Initialize the class
h.station_ip = "192.168.1.12"  # Your base station IP
h.get_state() # Authenticate, bootstrap your lighting system

for light in ('l1', 'l2', 'l3'):
	l = h.lights.get(light)
	l.off()

