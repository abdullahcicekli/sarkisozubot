import requests
from bs4 import BeautifulSoup

print("Kaç Sayfa  :")
sayfa=int(input())

sayac =1
for i in range(sayfa):
      url = "https://www.sarkisozleri.bbs.tr/" + str(i)

      r=requests.get(url)

      soup = BeautifulSoup(r.content,"lxml")

      sarkilar = soup.find_all("div",attrs={"class":"kutu1 esit-olsun-bakalim"})
      #elenmis = sarkilar.find_all("div",attrs={"class":"kutu1 esit-olsun-bakalim"})
      #print(elenmis)

      for sarki in sarkilar:
          sayac+=1
          sarkiAdi = (sarki.a.text)
          sanatci = (sarki.find("a",attrs={"class":"text-muted"}).text)
          link= "https://www.sarkisozleri.bbs.tr/"+ sarki.a.get("href")

          sarki_r = requests.get(link)
          sarki_soup = BeautifulSoup(sarki_r.content,"lxml")
          sarkisozu = sarki_soup.find("div",attrs={"class":"well"}).select("div:nth-of-type(1)> div:nth-of-type(1)")[1].text.strip( )

          print("Şarkı Adı : {}\nŞanatçı : {}\nŞarkı Sözleri : \n\n {}".format(sarkiAdi,sanatci,sarkisozu))
          print("*"*70)
          dosya = open((sarkiAdi)+".txt","w")
          dosya.write("Şarkı Adı : {}\nŞanatçı : {}\nŞarkı Sözleri : \n\n {}".format(sarkiAdi,sanatci,sarkisozu))
          dosya.close()
