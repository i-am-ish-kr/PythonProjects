import pyqrcode #pip install pyqrcode
from pyqrcode import QRCode
s = input("Enter the URL: ")
url = pyqrcode.create(s)
url.svg("myQrCode.svg", scale=8)