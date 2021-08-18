from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
Soupurl="https://uae.souq.com/ae-en/shop-all-categories/c/?ref=nav"
uClient=uReq("https://uae.souq.com/ae-en/shop-all-categories/c/?ref=nav")
page_soup = BeautifulSoup(uClient.read(), "html.parser")
uClient.close()
container=page_soup.findAll("div",{"class":"grouped-list"})
my_dic={}
for con1 in container:
 demo=con1.find_all('a')
 for y in demo:
    demo1=y.text.strip()

    cat=con1.find_all('ul',{'class':'sub-shop-list'})
    for x in cat:
        try:
            demo2=x.find('li')
            names=demo2.text.strip()
            hirearchy=(demo1+"|"+names)
            for y in demo2:
                links=x.find('a')['href']
                my_dic[hirearchy]=links

        except:
            links="0"
for y in my_dic:
    print(y+":"+my_dic[y])
