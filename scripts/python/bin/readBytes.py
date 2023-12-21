import sys


#Input: takes a file that contains a utf8 bytestring such as `K\x80t-\xe2\xbf\x82\xac\xb3c\x00\x00\uffff\U000001`

#Output: Int:  [75, 128, 116, 45, 226, 191, 130, 172, 179, 99, 0, 0, 65535, 1, 10]
#        Hex:  0x4B80742DE2BF82ACB3630000FFFF0000010A


###documentation: https://github.com/runtimeverification/pyk/blob/c1da98b74b5d481cae83c45a206cba7a34aba5f6/src/pyk/utils.py#L357

def computeBytes(path: str):
    result_int = []
    result_hex = "0x"
    with open(path, "rb") as f:
        while (fst := f.read(1)):
            if (fst == b'\\'):
                (snd := f.read(1))
                if(snd == b'x'):
                    (bytes_1 := f.read(2))
                    value = int(bytes_1, base=16)
                elif (snd == b'u'):
                    (bytes_2 := f.read(4))
                    value = int(bytes_2, base=16)
                    result_int.append(value)
                    result_hex += "{0:0{1}X}".format(value,4)
                    continue
                elif (snd == b'U'):
                    (bytes_3 := f.read(6))
                    value = int(bytes_3, base=16)
                    result_int.append(value)
                    result_hex += "{0:0{1}X}".format(value,6)
                    continue
            else:
                value = ord(fst)
            
            result_int.append(value)
            result_hex += "{0:0{1}X}".format(value,2)

    print("Int: ", result_int)
    print("Hex: ", result_hex)
    print("Length: ", len(result_int))


if __name__ == "__main__":
    computeBytes(sys.argv[1])