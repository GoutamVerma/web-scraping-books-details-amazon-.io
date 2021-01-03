from bs4 import BeautifulSoup
import requests
import csv
header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15'}
def amazon(url,num):
    book=url.replace(" ","+")
    for i in range(num):
        url=f'https://www.amazon.in/s?k={book}&page={num}&qid=1609673380&ref=sr_pg_{num}'
        res=requests.get(url,headers=header)
        soup=BeautifulSoup(res.text,'html.parser')
        with open('books.csv','a') as file2:
            writer=csv.writer(file2)
            name=soup.select(".a-size-medium")
            for i in range(len(name)):
                lst=[]
                try:
                    price=soup.select(".a-spacing-top-small .a-price-whole")[i].get_text().strip()
                    if price!="":
                        name= soup.select('.a-color-base.a-text-normal')[i].get_text().strip()
                        link=soup.select(".a-link-normal")[i].attrs.get('href')
                except:
                    price=""
                    name=""
                lst=[name,price,link]
                writer.writerow(lst)

amazon(input("Book Name:"),int(input("Enter No of Pages:")))
