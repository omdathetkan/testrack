import smbus
import time

# I2C channel 1 is connected to the GPIO pins
I2C_CHANNEL = 1

# Board Configurations
POSITION_ALONE  = "alone"
POSITION_LEFT   = "left"
POSITION_MIDDLE = "middle"
POSITION_RIGHT  = "right"

MUX_ADDRESS = {
    POSITION_ALONE :  0x71,
    POSITION_LEFT :   0x70,
    POSITION_MIDDLE : 0x72,
    POSITION_RIGHT :  0x73,
}

HOTSWAP_ADDRESS =                                               {
    POSITION_ALONE :  [0x70, 0x70, 0x70, 0x70, 0x70, 0x70, 0x70, 0x70],
    POSITION_LEFT :   [0x54, 0x55, 0x56, 0x57, 0x5c, 0x5d, 0x5e, 0x5f],
    POSITION_MIDDLE : [0x64, 0x65, 0x66, 0x67, 0x6c, 0x6d, 0x6e, 0x6f],
    POSITION_RIGHT :  [0x44, 0x45, 0x46, 0x47, 0x4c, 0x4d, 0x4e, 0x4f],
}



def BIT(num):
    return 1 << num

class LTC4222:
    # Registers
    LTC4222_CONTROL1    = 0xd0
    LTC4222_ALERT1      = 0xd1
    LTC4222_STATUS1     = 0xd2
    LTC4222_FAULT1      = 0xd3
    LTC4222_CONTROL2    = 0xd4
    LTC4222_ALERT2      = 0xd5
    LTC4222_STATUS2     = 0xd6
    LTC4222_FAULT2      = 0xd7
    LTC4222_SOURCE1     = 0xd8
    LTC4222_SOURCE2     = 0xda
    LTC4222_ADIN1       = 0xdc
    LTC4222_ADIN2       = 0xde
    LTC4222_SENSE1      = 0xe0
    LTC4222_SENSE2      = 0xe2
    LTC4222_ADC_CONTROL = 0xe4

    # Fault register bits
    FAULT_OV            = BIT(0)
    FAULT_UV            = BIT(1)
    FAULT_OC            = BIT(2)
    FAULT_POWER_BAD     = BIT(3)
    FAULT_FET_BAD       = BIT(5)

    # Constants (in mv)
    RES_ADIN_MV         = 0.00125
    RES_SOURCE_MA       = 0.03125
    RES_SENSE_MV        = 0.0000625

    def __init__(self, bus, address, shunt_value):
        self.bus = bus
        self.address = address
        self.shunt_value = shunt_value

    # Return the voltage from the given register in mV or mA
    def get_value(self, reg):
        # Read word, Endianness swap, Shift right to remove padding
        val = self.bus.read_word_data(self.address, reg)
        val = ((val & 0xFF) << 8) + ((val & 0xFF00) >> 8)
        val = val >> 6

        if(reg in [self.LTC4222_ADIN1, self.LTC4222_ADIN2]):
            val = val * self.RES_ADIN_MV

        elif(reg in [self.LTC4222_SOURCE1, self.LTC4222_SOURCE2]):
            val = val * self.RES_SOURCE_MA

        elif(reg in [self.LTC4222_SENSE1, self.LTC4222_SENSE2]):
            val = val * self.RES_SENSE_MV

        else:
            raise ValueError

        return val;

    def get_voltage(self, channel):
        return self.get_value(self.LTC4222_SOURCE1 if channel == 1 else self.LTC4222_SOURCE2)

    def get_current(self, channel):
        return self.get_value(self.LTC4222_SENSE1 if channel == 1 else self.LTC4222_SENSE2) / self.shunt_value

    def get_status(self, channel):
        return self.bus.read_byte_data(self.address, self.LTC4222_STATUS1 if channel == 1 else self.LTC4222_STATUS2)

    def print_status(self, name):
        voltage1 = self.get_voltage(1)
        voltage2 = self.get_voltage(2)
        current1 = self.get_current(1)
        current2 = self.get_current(2)
        enabled1 = "X" if self.get_status(1) & 0x10 else "-"
        enabled2 = "X" if self.get_status(1) & 0x10 else "-"

        name = "{} [{:02x}]".format(name, self.address)

        return "{:} {} {:10.3f}V {:10.3f}A / {} {:10.3f}V {:10.3f}A\n".format(name, enabled1, voltage1, current1, enabled2, voltage2, current2)


class TCA9548:
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address

    def set(self, value):
        self.bus.write_byte(self.address, value)

    def get(self):
        return self.bus.read_byte(self.address)

class Backplane:
    BOARDS = [POSITION_RIGHT, POSITION_MIDDLE, POSITION_LEFT]
    SHUNT_VALUE_MAIN = 0.01
    SHUNT_VALUE_SLOT = 0.025

    def __init__(self, bus):
        slots = sum([HOTSWAP_ADDRESS[x][1:8] for x in self.BOARDS], [])
        self.mux = [TCA9548(bus, MUX_ADDRESS[x]) for x in self.BOARDS]
        self.main = [LTC4222(bus, HOTSWAP_ADDRESS[x][0], self.SHUNT_VALUE_MAIN) for x in self.BOARDS]
        self.slots = [LTC4222(bus, s, self.SHUNT_VALUE_SLOT) for s in slots]

    def mux_status(self):
        for m in self.mux:
            print("Mux {:02x} = {:02x}".format(m.address, m.get()))

    def power_status(self):
        buf = "----------\n"

        for num, m in enumerate(self.main):
            buf += m.print_status("M{}--".format(num))
        for num, s in enumerate(self.slots):
            seg = int(num / 7)
            pos = num % 7
            if pos == 0:
                buf += "\n"
            buf += s.print_status("S{:}-{:}".format(seg+1, pos+1))

        print(buf)

# Initialize I2C (SMBus)
bus = smbus.SMBus(I2C_CHANNEL)

plane = Backplane(bus)
plane.mux_status()

while 1:
    plane.power_status()
    time.sleep(0.5)