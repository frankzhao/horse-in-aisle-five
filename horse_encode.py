import os
import sys
import bitstring

usage = "Usage: python horse_encode.py [filename]"
zero = "There's a horse in aisle five."
one = "My house is full of traps."

if len(sys.argv) != 2:
    print(usage)
else:
    filename = sys.argv[1]
    init_size = os.path.getsize(filename)
    print("Initial size: " + str(init_size) + " bytes")
    f = open(filename, "rb")
    try:
        binary = bitstring.Bits(f).bin

        f_out = open(filename + ".horse", "w")
        for b in binary:
            if int(b) == 0:
                f_out.write(zero)
            else:
                f_out.write(one)
        print("Encoded size: " + str(f_out.tell()) + " bytes")
        print("Compression ratio: " + str((f_out.tell()/init_size)*100) + "%")
        f_out.close()

    finally:
        f.close
