import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://cic.tju.edu.cn/english/faculty/Search_by_College.htm"
pagehtml = requests.get(url)  # open the url and grabbing the page
pagehtml.encoding = 'utf-8'
page_soup = BeautifulSoup(pagehtml.text, "lxml")  # parsing the html
print(page_soup)

listaLink = page_soup.select("body > div.m > div > div.con_ny_r > div > div.con_list_body > ul > li > a")

puzzlePiece = "http://cic.tju.edu.cn/"
finaLink = []

for i in listaLink:
    info = {
        finaLink.append(puzzlePiece + i.get("href"))
    }

a = 0
sopa = []
for i in finaLink:
    molho = requests.get(finaLink[a])
    molho.enconding = 'utf-8'
    resultado = BeautifulSoup(molho.text, "lxml")
    sopa += resultado.select("#vsb_content > div")
    #for paragraph in sopa[a].find_all('p'):
        #print(paragraph.text)
    #print(
        #"___________________________________________________________________________________________________")
    #a = a + 1
