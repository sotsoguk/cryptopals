from base64 import b64encode, b64decode

# cryptopals set 1

def hexStringToBase64(s):
    return b64encode(bytearry.fromhex(s))

def fixedXor(s1, s2):
    bs1, bs2 = bytes.fromhex(s1), bytes.fromhex(s2)
    assert(len(bs1) == len(bs2))
    return bytes([a^b for a,b in zip(bs1,bs2)])

def singleByteXor(s1,sx):
    bs1, bsx = bytes.fromhex(s1), bytes.fromhex(sx)
    return bytes([a^bsx for a in bs1])

 