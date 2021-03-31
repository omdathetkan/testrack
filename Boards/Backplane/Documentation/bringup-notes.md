    Power up board
        Current draw 5ma @ 24V
        V_IN_24P0 is present
        No power on V_2P1, V_3P3, V_24P0, V_REG_5P0 
        Turned out LTC4222 creates power from VDD2 which is 5V
        5V not working, investigate
        5V buck 24V input not working because it is gated by LTC
        Hot wired primary 24V switch, board seems to board (with some parks), needs around 300mA for startup, needs design change :warning: 
        Current draw 100mA @ 24V
        Power rails seem stable. Pgood leds inverted? :warning: 
    Test USB Host
        Create USB host harness (make sure A3 is connected to ground)
        “USB device not recognized” - Device descriptor request failed
        V_USB_1P8 stable, V_USB_PLL_1P8 is 0V 
        Lifted EEPROM(U105) SDA/SCL pins
        RESET_N = 3.3V
        Compare schematic against evb2517sch.pdf
        Flipped D+/D-, now obviously works
        TODO: revert SCL/SDA? Depopulate on PCB? :warning: 
    Test LAN switch
        Plug in port 8 to laptop, no response
        Magjack led polarity reversed on footprint :warning: 
    Hot Swap Controllers
        INTVCC is ok
        Outputs are note enabled → enable was not connected
        All good
    Daisy chain
        Slots are too short :warning: 
        Middle slot is shifted :warning: 
        Add arrow master/slave silkscreen :warning: 
        For 3 boards 650ma is needed to power up, 300mA nominal
    Misc
        Add project name to silkscreen
        Airflow? Check heat on power supply etc
 
TODO:
- Create labels.....

Enable USB:
/boot/config.txt: add
dtoverlay=dwc2,dr_mode=host

https://pinout.xyz/pinout/i2c#
python example

pi@raspberrypi:~ $ lsusb
Bus 001 Device 004: ID 0424:2517 Standard Microsystems Corp. Hub
Bus 001 Device 003: ID 0424:2517 Standard Microsystems Corp. Hub
Bus 001 Device 002: ID 0424:2514 Standard Microsystems Corp. USB 2.0 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

i2cset -y 1 0x73 0x01
i2cset -y 1 0x72 0x01
i2cset -y 1 0x70 0x01


pi@raspberrypi:~ $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- 44 45 46 47 -- -- -- -- 4c 4d 4e 4f
50: -- -- -- -- 54 55 56 57 -- -- -- -- 5c 5d 5e 5f
60: -- -- -- 63 64 65 66 67 -- -- -- -- 6c 6d 6e 6f
70: 70 -- 72 73 -- -- -- --

Note: 0x63 = Call All LTC

----------
M0-- [44] X     21.594V      0.100A / X      5.094V      0.000A
M1-- [64] X     21.844V      0.000A / X      5.094V      0.000A
M2-- [54] X     21.844V      0.413A / X      5.031V      0.306A

S1-1 [45] -      0.000V      0.000A / -      0.000V      0.000A
S1-2 [46] -      0.000V      0.000A / -      0.000V      0.000A
S1-3 [47] -      0.000V      0.000A / -      0.000V      0.000A
S1-4 [4c] -      0.000V      0.000A / -      0.000V      0.000A
S1-5 [4d] -      0.000V      0.000A / -      0.000V      0.000A
S1-6 [4e] -      0.000V      0.000A / -      0.000V      0.000A
S1-7 [4f] -      0.000V      0.000A / -      0.000V      0.000A

S2-1 [65] -      0.000V      0.000A / -      0.000V      0.000A
S2-2 [66] -      0.000V      0.000A / -      0.000V      0.000A
S2-3 [67] -      0.000V      0.000A / -      0.000V      0.000A
S2-4 [6c] -      0.000V      0.000A / -      0.000V      0.000A
S2-5 [6d] X      5.062V      0.000A / X     21.781V      0.003A (Niels Radio test board)
S2-6 [6e] -      0.000V      0.000A / -      0.000V      0.000A
S2-7 [6f] -      0.000V      0.000A / -      0.000V      0.000A

S3-1 [55] -      0.000V      0.000A / -      0.000V      0.000A
S3-2 [56] -      0.000V      0.000A / -      0.000V      0.000A
S3-3 [57] -      0.000V      0.000A / -      0.000V      0.000A
S3-4 [5c] -      0.000V      0.000A / -      0.000V      0.000A
S3-5 [5d] -      0.000V      0.000A / -      0.000V      0.000A
S3-6 [5e] -      0.000V      0.000A / -      0.000V      0.000A
S3-7 [5f] X      5.031V      0.250A / X     21.844V      0.000A (PI)
