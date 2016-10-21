start = 1000001 - 2

def numisprime(num):
	if num % 2 == 0:
		return False
	for q in range(3, num+1, 2):
		#print(str(num)+'%'+str(q)+'='+str(num%q))
		if q == num:
			#print('found one: ' + str(num))
			#reak
			return True
		if num % q == 0:
			break

def findprime(start):
	for num in range(start+2, start*10, 2):
		print(num)
		if numisprime(num) == True and sumofdigitsisprime(num) == True:
			return num
		
def sumofdigitsisprime(num):
	sd = 0
	for char in str(num):
		sd += int(char)
	if numisprime(sd) == True:
		return True
	else:
		return False


first = findprime(start)
second = findprime(first)
	
print(first, second)
#print(sumofdigitsisprime(1590))
