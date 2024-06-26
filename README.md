# DW1000 UWB-Ranging Library or Raspberry Pi, written in Python

This is a soft fork of the following repository: https://github.com/pedestrian0423/DW1000_Raspi_Python_library

The module provides both an RangingAnchor and a RangingTag class, both of which need to be executed on different Raspberry Pis to get a UWB communication between these Pis working.
Also needed are the DW1000 UWB modules, previously built by Decaware, now by Qorvo.
The goal of this is to have an ongoing communication between one Anchor and 1+ Tags. This was tested with 1/2 Tags, but you are free to find out the upper limit.

## Hardware
This was tested and run on both Pis 3B and 2. It can maybe be run on other variants as well, but due to budget and time constraints we only got to test this on 3s and 2s.
Also of course a DW1000 UWB module is needed, which has to be connected to the GPIO pins on the Pi.
We used standard wires for that, and soldered them to the DW1000, so those wires can then be put on to the pins on the Pi.

## Wiring
According to https://pinout.xyz/ and https://www.mouser.de/datasheet/2/412/DWM1000_Data_Sheet-1950396.pdf

| Function     | DW1000 Pin                 | DW1000 Pin Name | Pi Pin | Pi GPIO Pin |
|--------------|----------------------------|-----------------|--------|-------------|
| 3.3V         | 6 (7 also possible)        | VDD3V3          | 1      |             |
| GND          | 8 (16,23,24 also possible) | VSS             | 6      |             |
| Slave Select | 17                         | SPICSn          | 24     | 8           |
| MOSI         | 18                         | SPIMOSI         | 19     | 10          |
| MISO         | 19                         | SPIMISO         | 21     | 9           |
| Clock        | 20                         | SPICLK          | 23     | 11          |
| Interrupt    | 22                         | IRQ / GPIO8     | 29     | 5           |


## Additional info
While the original repository uses a manual slave select, we found no success in that, instead we rewrote the code so that we dont need to manually interact with the slave select and write/read all bits and bytes one by one, but can just push/pull our data as a full block.

### Original Code
As far as we could gather, originally this code is bases on a post on the no longer existing blog "ThingType".
Luckily the web archive has copies of this block post, the newest version of which can be accessed here: https://web.archive.org/web/20180701143031/https://thingtype.com/blog/using-a-dwm1000-module-with-a-raspberry-pi-and-python/