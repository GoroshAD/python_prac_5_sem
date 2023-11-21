import struct
print(" ".join(map(hex, list(struct.pack("bhl", 5, 0x432, 0x234234)))))
