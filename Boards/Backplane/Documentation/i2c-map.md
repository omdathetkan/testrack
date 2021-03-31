# Board global address nets

A is made from A0 and A1 using N-Fet?

| Board  | A0 | A1 | A   |
|--------|----|----|-----|
| Left   | H  | H  | L   |
| Middle | L  | H  | NC  |
| Right  | H  | L  | H   |


# I2C Mux - TCA9548

| A2 | A1 | A0 | Address | Binary    | Position         |
|----|----|----|---------|-----------|------------------|
| L  | L  | L  | 0x70    | 0b1110000 | Board 0          |
| L  | L  | H  | 0x71    | 0b1110001 | Board 1          |
| L  | H  | L  | 0x72    | 0b1110010 | Board 2          |
| L  | H  | H  | 0x73    | 0b1110011 |                  |
| H  | L  | L  | 0x74    | 0b1110100 |                  |
| H  | L  | H  | 0x75    | 0b1110101 |                  |
| H  | H  | L  | 0x76    | 0b1110110 |                  |
| H  | H  | H  | 0x77    | 0b1110111 |                  |

# Hot Swap Controllers - LTC4222

| A2 | A1 | A0 | Address | Binary    | Position         |
|----|----|----|---------|-----------|------------------|
| X  | X  | X  | C6      | 0b1100011 |                  |
| X  | X  | X  | 19      | 0b0001100 |                  |
| L  | NC | L  | 88      | 0b1000100 | Board 0 - In     |
| L  | H  | NC | 8A      | 0b1000101 | Board 0 - Slot 1 |
| L  | NC | NC | 8C      | 0b1000110 | Board 0 - Slot 2 |
| L  | NC | H  | 8E      | 0b1000111 | Board 0 - Slot 3 |
| L  | L  | L  | 98      | 0b1001100 | Board 0 - Slot 4 |
| L  | H  | H  | 9A      | 0b1001101 | Board 0 - Slot 5 |
| L  | L  | NC | 9C      | 0b1001110 | Board 0 - Slot 6 |
| L  | L  | H  | 9E      | 0b1001111 | Board 0 - Slot 7 |
| NC | NC | L  | A8      | 0b1010100 | Board 1 - In     |
| NC | H  | NC | AA      | 0b1010101 | Board 1 - Slot 1 |
| NC | NC | NC | AC      | 0b1010110 | Board 1 - Slot 2 |
| NC | NC | H  | AE      | 0b1010111 | Board 1 - Slot 3 |
| NC | L  | L  | B8      | 0b1011100 | Board 1 - Slot 4 |
| NC | H  | H  | BA      | 0b1011101 | Board 1 - Slot 5 |
| NC | L  | NC | BC      | 0b1011110 | Board 1 - Slot 6 |
| NC | L  | H  | BE      | 0b1011111 | Board 1 - Slot 7 |
| H  | NC | L  | C8      | 0b1100100 | Board 1 - In     |
| H  | H  | NC | CA      | 0b1100101 | Board 1 - Slot 1 |
| H  | NC | NC | CC      | 0b1100110 | Board 1 - Slot 2 |
| H  | NC | H  | CE      | 0b1100111 | Board 1 - Slot 3 |
| H  | L  | L  | D8      | 0b1101100 | Board 1 - Slot 4 |
| H  | H  | H  | DA      | 0b1101101 | Board 1 - Slot 5 |
| H  | L  | NC | DC      | 0b1101110 | Board 1 - Slot 6 |
| H  | L  | H  | DE      | 0b1101111 | Board 1 - Slot 7 |
| L  | H  | L  | E8      | 0b1110100 |                  |
| NC | H  | L  | EA      | 0b1110101 |                  |
| H  | H  | L  | EC      | 0b1110110 |                  |

# UID

| A2 | A1 | A0 | Address | Binary    | Device           |
|----|----|----|---------|-----------|------------------|
| -  | H  | L  | C8      | 0b1010000 | Board 1          |
| -  | H  | L  | C8      | 0b1010000 | Board 2          |
| -  | H  | L  | C8      | 0b1010000 | Board 3          |



# USB Hub

| A2 | A1 | A0 | Address | Binary    | Device           |
|----|----|----|---------|-----------|------------------|
| -  | -  | -  | C6      | 0b1010000 | EEPROM           |
| -  | -  | -  | 19      | 0b0101100 | Hub              |


# Ethernet Switch

| A2 | A1 | A0 | Address | Binary    | Device           |
|----|----|----|---------|-----------|------------------|
| -  | -  | -  | C6      | 0b1010000 | EEPROM           |
| -  | -  | -  | 19      | 0b0101100 | Switch           |

https://www.tablesgenerator.com/markdown_tables