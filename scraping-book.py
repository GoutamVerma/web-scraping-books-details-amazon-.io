import requests
from bs4 import BeautifulSoup
import csv
url='https://www.tutorialspoint.com/cprogramming/index.htm'
res=requests.get(url)
side_bar=[]
soup=BeautifulSoup(res.text,'html.parser')
for i in range(0,len(soup.select(".chapters a"))):
    side_bar_text=soup.select(".chapters a")[i].getText().strip()
    side_bar_text=side_bar_text.replace(" - ","_").lower()
    side_bar.append(side_bar_text)
side_bar=side_bar[1:]
side_bar[0]="index"
page=side_bar[2]
content=""
for i in range(0,len(side_bar)):
    page=side_bar[i]
    page=page.replace(" ","_")
    url=f"https://www.tutorialspoint.com/cprogramming/{page}.htm"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    data=soup.select("h2,p")
    for i in range(0,len(data)):
        content= content+(data[i].getText())
        content=content+"\n"
        content=content.replace("\u2212","")
        content = content.replace("\u2192","")
    f=open("c_notes_tutorials_point.txt",'a')
    f.write(content)
    f.close()
