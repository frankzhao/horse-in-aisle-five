import sys
import re
import bitarray

usage = "Usage: python horse_decode.py [filename]"
zero = "There's a horse in aisle five."
one = "My house is full of traps."

if len(sys.argv) != 2:
    print(usage)
else:
    filename = sys.argv[1]
    f = open(filename, "r")
    try:
        contents = f.read()
        contents = contents.replace(zero, '0')
        contents = contents.replace(one, '1')
        contents = bitarray.bitarray(contents)

        f_out = open(re.sub(r"horse$", "unhorse", filename), "wb")
        f_out.write(contents)

    finally:
        f.close
