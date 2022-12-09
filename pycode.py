from asyncio.windows_events import NULL
from pickle import APPEND
from urllib import response
from bs4 import BeautifulSoup
import requests
import pandas as pd 

from asyncio.windows_events import NULL
from pickle import APPEND
from urllib import response
from bs4 import BeautifulSoup
import requests
import pandas as pd
#lst=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#pv=[970,275,894,528,406,349,329,133,211,59,177,436,604,399,429,582,44,560,538,550,101,285,80,66,23,260]
lst=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
pv=[970,275,894,528,406,349,329,133,211,59,177,436,604,399,429,582,44,560,538,550,101,285,80,66,23,260]
m=-1
for l in lst:
    m=m+1
    print("Start Alphabet:"+l)
    for x in range(1,pv[m]):
       
            nme=[]
            pdet=[]
            manc=[]
            compdet=[]
            pdlnk=[]
            mrp=[]
            
            url="https://www.1mg.com/drugs-all-medicines?page="+str(x)+"&label="+l
            r=requests.get(url)
            htmlcontent=r.content
            soup = BeautifulSoup(htmlcontent, 'html.parser')
            table=soup.find_all("div",{"class":"Card__container__liTc5 Card__productCard__SrdLF Card__direction__H8OmP container-fluid-padded-xl"})
            for i in table:
                soup2=BeautifulSoup(str(i),'lxml')
                nm=soup2.find("p",{"class":"Card__productName__qw2CE bodyMedium"})
                
                det=soup2.find_all("p",{"class":"Card__productDescription__kL6Ho"})
                if len(det)!=3:
                    pdd=det[1].getText()
                
                    man=det[2].getText()
                
                    comp=det[3].getText()
                else:    
                    pdd=det[0].getText()
                
                    man=det[1].getText()
                
                    comp=det[2].getText()
                lnk=soup2.find(class_='Card__productCard__SrdLF marginTop-4 Card__text__jeyhg', href=True)
                    #
                price=soup2.find("span",{"class":"l3Regular"})
                pdlnk.append(lnk['href'])
                nme.append(nm.getText())
                pdet.append(pdd)
                manc.append(man)
                compdet.append(comp)
                mrp.append(price.getText())
                #print(nm.getText()+"-"+lnk['href']+"-"+pd+man+comp)
                
                
                
            dict = { 'Name': nme,'Product Details':pdet,'Manufacturer':manc,'Compsition':compdet,'MRP':mrp,'Product Link':pdlnk }  
            df = pd.DataFrame(dict)  
            df.to_csv('F:\\MEDICINE_DATA_TATA1MG_new.csv',mode='a', header=False) 
            #print("Page Done no.:"+str(i))

            print("Page Done For:"+l+"--"+str(x))
