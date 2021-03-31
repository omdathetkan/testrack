| QFN (RGE) | PCB NET | NAME  | TYPE  | DESCRIPTION                                                                                  |
|-----------|---------|-------|-------|----------------------------------------------------------------------------------------------|
|     1     | SC0   X | SD0   |  I/O  | Serial data 0. Connect to VDPU0(1)   through a pull-up resistor                              |
|     2     | SC1   X | SC0   |  I/O  | Serial clock 0.   Connect to VDPU0(1) through a pull-up resistor                             |
|     3     | SC2   X | SD1   |  I/O  | Serial data 1.   Connect to VDPU1(1) through a pull-up resistor                              |
|     4     | SC3   X | SC1   |  I/O  | Serial clock 1.   Connect to VDPU1(1) through a pull-up resistor                             |
|     5     | SC4   X | SD2   |  I/O  | Serial data 2.   Connect to VDPU2(1) through a pull-up resistor                              |
|     6     | SC5   X | SC2   |  I/O  | Serial clock 2.   Connect to VDPU2(1) through a pull-up resistor                             |
|     7     | SC6   X | SD3   |  I/O  | Serial data 3.   Connect to VDPU3(1) through a pull-up resistor                              |
|     8     | SC7   X | SC3   |  I/O  | Serial clock 3.   Connect to VDPU3(1) through a pull-up resistor                             |
|     9     | GND     | GND   |   —   | Ground                                                                                       |
|     10    | SCL   X | SD4   |  I/O  | Serial data 4.   Connect to VDPU4(1) through a pull-up resistor                              |
|     11    | SD0   X | SC4   |  I/O  | Serial clock 4.   Connect to VDPU4(1) through a pull-up resistor                             |
|     12    | SD1   X | SD5   |  I/O  | Serial data 5.   Connect to VDPU5(1) through a pull-up resistor                              |
|     13    | SD2   X | SC5   |  I/O  | Serial clock 5.   Connect to VDPU5(1) through a pull-up resistor                             |
|     14    | SD3   X | SD6   |  I/O  | Serial data 6.   Connect to VDPU6(1) through a pull-up resistor                              |
|     15    | SD4   X | SC6   |  I/O  | Serial clock 6.   Connect to VDPU6(1) through a pull-up resistor                             |
|     16    | SD5   X | SD7   |  I/O  | Serial data 7.   Connect to VDPU7(1) through a pull-up resistor                              |
|     17    | SD6   X | SC7   |  I/O  | Serial clock 7.   Connect to VDPU7(1) through a pull-up resistor                             |
|     18    | A2      | A2    |   I   | Address input 2.   Connect directly to VCC or ground                                         |
|     19    | SD7   X | SCL   |  I/O  | Serial clock bus.   Connect to VDPUM(1) through a pull-up resistor                           |
|     20    | SDA     | SDA   |  I/O  | Serial data bus.   Connect to VDPUM(1) through a pull-up resistor                            |
|     21    | VCC     | VCC   | Power | Supply voltage                                                                               |
|     22    | A0      | A0    |   I   | Address input 0.   Connect directly to VCC or ground                                         |
|     23    | A1      | A1    |   I   | Address input 1.   Connect directly to VCC or ground                                         |
|     24    | RESET   | RESET |   I   | Active-low reset   input. Connect to VCC or VDPUM(1) through a pull-up resistor, if not used |