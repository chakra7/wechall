import requests

link = 'https://www.wechall.net/challenge/training/programming1/index.php?action=request'

r = requests.get(link, cookies={'WC': '9127167-21232-7XaJbL1I5qjptC2I'})
#print(r.content)
target = 'https://www.wechall.net/challenge/training/programming1/index.php?answer='+r.content

r2 = requests.get(target, cookies={'WC': '9127167-21232-7XaJbL1I5qjptC2I'})
print(r2.content) 
