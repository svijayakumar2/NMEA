import time
import serial
import string
from pynmea2 import nmea

ser = serial.Serial()
ser.port = "COM7"
ser.baudrate = 115200
ser.timeout = 1
ser.open()
gpgga = nmea.GPGGA()
while True:
    data = ser.readline()
    if data[0:6] == '$GPGGA':
        ##method for parsing the sentence
        gpgga.parse(data)
	#latitude values
        lats = gpgga.latitude
	#latitude direction
        lat_dir = gpgga.lat_direction
	#longitude values
        longitude = gpgga.longitude
	#longitude direction
        long_dir = gpgga.lon_direction
	#GPS time stamp
        time_stamp = gpgga.timestamp

	#antenna altitude
        alt = gpgga.antenna_altitude

        lat_deg = lats[0:2]
        lat_mins = lats[2:4]
        lat_secs = round(float(lats[5:])*60/10000, 2)
	
	#latitude string
        latitude_string = lat_deg + u'\N{DEGREE SIGN}' + lat_mins + string.printable[68] + str(lat_secs) + string.printable[63]
	
	
        lon_deg = longitude[0:3]
        lon_mins = longitude[3:5]
        lon_secs = round(float(longitude[6:])*60/10000, 2)
	#longitude
        lon_str = lon_deg + u'\N{DEGREE SIGN}' + lon_mins + string.printable[68] + str(lon_secs) + string.printable[63]
	ser.write(newdata)
