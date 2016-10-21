prime_url = 'http://www.wechall.net/challenge/impossible/index.php?request=new_number'
sol = ''

def numisprime(num):
	if num % 2 == 0:
		sol += '2'
	for q in range(3, num+1, 2):
		#print(str(num)+'%'+str(q)+'='+str(num%q))
		if q == num:
			#print('found one: ' + str(num))
			#reak
			sol = str(num)
		if num % q == 0:
			
