# 2024.03.23
# Source: https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio
# check address of the Pluto device "iio_info -s"

import adi
import time

# Create radio object
sdr = adi.Pluto ( uri = "usb:2.6.5" )
# sdr = adi.Pluto ('ip:192.168.2.1' )
print ( sdr )

# Configure properties
sdr.rx_rf_bandwidth = 4000000

# Get data
print ( sdr.rx_hardwaregain_chan0 )
data = sdr.rx ()
print ( data )
while True :
    print ( sdr.rx_hardwaregain_chan0 )
    time.sleep ( 3 )
    print ( data )