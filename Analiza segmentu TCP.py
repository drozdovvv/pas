d = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
datagram = d.replace(" ", "")
numer_zr_portu = int(datagram[:4], 16)
numer_dc_portu = int(datagram[4:8], 16)
header_l = int(datagram[24:25], 16)
print(bytes.fromhex(datagram[header_l*8:]).decode('utf-8'))
