from enum import Enum

class CodeType(str, Enum):
    QR = "QR Code"
    EAN13 = "EAN13"
    CODE128 = "Code128"
