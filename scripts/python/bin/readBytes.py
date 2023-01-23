import sys
import os

def computeBytes(func:bytes):
    i = 0
    result_int = []
    result_hex = "0x"
    while (i < len(func)):
        c=func[i]
        if (c == '\\'):
            hex_group = func[i+2:i+4]
            value = int(hex_group, base=16)
            i += 4
        else:
            value = ord(c)
            i += 1
        result_int.append(value)
        result_hex += hex(value)[2:]

    print("Int: ", result_int)
    print("Hex: ", result_hex)

if __name__ == "__main__":
    computeBytes(sys.argv[1])

