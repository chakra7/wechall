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
	d = decrypto('ESP BFTNV MCZHY QZI UFXAD ZGPC ESP WLKJ OZR ZQ NLPDLC LYO JZFC FYTBFP DZWFETZY TD SZPLDLPAXTDO', i)
	print(d)
		
		
