# 2024.03.23
# install libiio-<version>-setup.exe from https://github.com/analogdevicesinc/libiio/releases
# install python module python -m pip install pyadi-iio
# Source: https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio
# Check address of the Pluto device: iio_info -s
# Full info about device: iio_info -u ip:192.168.2.1 or iio_info -u usb:2.14.5
# Check the firmware version: iio_attr -u usb:2.14.5 -C fw_version
# List devices in an IIO context: iio_attr -u usb:2.14.5 -d

import adi
import time

# Create radio object
sdr = adi.Pluto ( uri = "usb:" )
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
