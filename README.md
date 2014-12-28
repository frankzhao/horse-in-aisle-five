horse-in-aisle-five
===================

Novel file 'compression' method from XKCD's "What If?" series. Original here: [http://what-if.xkcd.com/34/].

How it works
===
Zeros get encoded into the string `"There's a horse in aisle five."`. Ones get encoded into the string `"My house is full of traps."`. Simple.

Dependencies
===
- bitarray
- bitstring

Running
===
Encode a file
`python horse_encode.py [filename]`
The encoded file will be named `filename.horse`.

Decode a file
`python horse_decode.py [filename]`
The encoded file will be named `filename.unhorse`.