encs ='MX UZG VQCFOZUX OIA XIH JVY NGVA UZFB CX TNFGYA F VC FCPNGBBGA WGNX DGQQ AIYG XIHN BIQHUFIY EGX FB CYIYIFYIBPPV UZFB QFUUQG JZVQQGYOG DVB YIU UII ZVNA DVB FU'

allchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypto(encs, shift):
	decs = ''
	for char in encs:
		if char == ' ':
			decs += char
		else :
			# 65 + (k-65) % 26
			decs += str(unichr(65 + (ord(char) + shift - 65)%26))
	return decs


for i in range(1, 26):
	d = decrypto(encs, i)
	print(d)
