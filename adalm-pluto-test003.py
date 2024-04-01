# https://pysdr.org/content/pluto.html

import numpy as np
import adi

sample_rate = 1e6 # Hz
center_freq = 70e6 # Hz
num_samps = 10000 # number of samples returned per call to rx()

sdr = adi.Pluto ( uri = "usb:2.16.5" )

sdr.gain_control_mode_chan0 = "slow_attack"
sdr.rx_lo = int ( center_freq )

print (sdr.rx_lo)
sdr.sample_rate = int(sample_rate)
sdr.rx_rf_bandwidth = int(sample_rate) # filter width, just set it to the same as sample rate for now
sdr.rx_buffer_size = num_samps

samples = sdr.rx() # receive samples off Pluto
print(samples[0:10])