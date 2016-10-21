import requests

inj = 'bill'
target= 'https://www.wechall.net/challenge/no_escape/index.php?vote_for='+inj

for i in range(100):
	r = requests.get(target, cookies={'WC': '9127167-21232-7XaJbL1I5qjptC2I'})

