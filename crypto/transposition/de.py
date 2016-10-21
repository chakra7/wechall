encs = 'oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wc aahfsosiha.s'
#print(len(encs))
#encsmod = encs.replace(' ', '').replace('.', '').replace(':', '')
#print(encsmod[:29])
#print(encsmod[30:89])
#print(encsmod[90:118])
#print(len(encsmod)) 

decs = ''

for i in range(0, len(encs), 2):
	s = encs[i:i+2]
	decs += s[::-1]

print(decs)	
	
