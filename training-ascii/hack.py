arr = [84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 102, 111, 104, 102, 103, 109, 110, 104, 109, 105, 97, 102]

decs = ''
for i in arr:
	decs += str(unichr(i))

print(decs)
	
