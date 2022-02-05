import requests,html5lib,os,re
from bs4 import BeautifulSoup



content=input("serach : ").split()
url="https://thepiratebay.party/search/"
for i in content:
    if  content[-1]==i:
        url+=i
    else:
        url+=i
        url+="%20"


r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')

# gets magnet links
magnet=open("magnet.txt",'w')
magnet.truncate()
for maglink in soup.find_all("a",title="Download this torrent using magnet"):
    magnet.write(maglink.get("href"))
    magnet.write("\n")
magnet.close()

# gets title
title=open("title.txt",'w')
title.truncate()
reg=re.compile(r'Details for')
reg1=re.compile(r'(title="Details for )(.*)(")')
for titl in soup.find_all("a"):
    title1=reg.search(str(titl.get("title")))
    if title1:
         fintit=reg1.search(str(titl)) 
         title.write(fintit.group(2)+"\n")
title.close()

title=open("title.txt",'r')
count=1
for line in  title:
    print(str(count)+". "+line)
    count+=1
title.close()
choice=int(input("select : "))

magnet=open("magnet.txt",'r')
magstr=magnet.readlines()
os.startfile(magstr[choice])