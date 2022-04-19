from base64 import b64encode, b64decode
from collections import defaultdict

from sqlalchemy import Float
# cryptopals set 1


def hexStringToBase64(s):
    return b64encode(bytearray.fromhex(s))

def fixedXor(s1, s2):
    bs1, bs2 = bytes.fromhex(s1), bytes.fromhex(s2)
    assert(len(bs1) == len(bs2))
    return bytes([a^b for a,b in zip(bs1,bs2)])

def singleByteXor(s1,sx):
    bs1, bsx = bytes.fromhex(s1), bytes.fromhex(sx)
    return bytes([a^bsx for a in bs1])

class letterScorer():
    loc_en = """E	12.60
T	9.37
A	8.34
O	7.70
N	6.80
I	6.71
H	6.11
S	6.11
R	5.68
L	4.24
D	4.14
U	2.85
C	2.73
M	2.53
W	2.34
Y	2.04
F	2.03
G	1.92
P	1.66
B	1.54
V	1.06
K	0.87
J	0.23
X	0.20
Q	0.09
Z	0.06"""
    def __init__(self,locale = "en") -> None:
        self.locale = self.loc_en
        self.counter = defaultdict(int)
        self.freqDict = self._initDict()
        self.score = 0.0
        self.len = 0

    def _initDict(self):
        d = dict()
        for tok in self.locale.split("\n"):
            (ch,freq) = tok.split("\t")
            d[ch.lower()] = float(freq)
        return d

    def count(self,str):
        for c in str:
            self.counter[c] += 1 
            self.len += 1
    def resetCounter(self):
        self.counter = defaultdict(int)
        self.score = 0.0
        self.len = 0

    def calcScore(self) -> Float:
        for c, cnt in self.counter.values():
            isup