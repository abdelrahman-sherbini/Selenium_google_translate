# import requests

# url = "https://translate.yandex.com/api/v1.5/tr.j\
# son/translate?keytrnsl.1.1.20190821T231506Z.0ce703d4a746fde.5dcbab81dac6133800dc76f34b8241526fc369a7&test=sky is clear&lang=en-ar"

# payload = "apiKey=%3CREQUIRED%3E&text=%3CREQUIRED%3E"
# headers = {
#     'content-type': "application/x-www-form-urlencoded",
#     'x-rapidapi-key': "SIGN-UP-FOR-KEY",
#     'x-rapidapi-host': "YandexTranslatezakutynskyV1.p.rapidapi.com"
#     }

# response = requests.request("GET", url)

# print(response.text)
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome('./chromedriver')
string = "sky is clear"
# driver.get("https://translate.google.com/?sl=en&tl=ar&text="+string+"&op=translate")
# search_bar = driver.find_element_by_class_name("VIiyi")
# print(search_bar)
# import bs4
# import urllib.request
# import urllib.parse
# print("https://translate.google.com/?sl=en&tl=ar&text="+urllib.parse.quote(string)+"&op=translate")
# a_website = urllib.request.urlopen("https://translate.google.com/?sl=en&tl=ar&text="+urllib.parse.quote(string)+"&op=translate")
# a_soup = bs4.BeautifulSoup(a_website)
# mydivs = a_soup.find_all("div", {"class": "VIiyi"})
# print(mydivs)
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from pyarabic.araby import normalize_ligature
import pyarabic.araby as araby
import arabic_reshaper
from bidi.algorithm import get_display
import time
start = time.time()
file1=open('C:\\Users\\abdel\\OneDrive\\Desktop\\koloh\\4th year\\Flickr8k_text\\tst.txt','r',encoding='utf-8')
file2=open('C:\\Users\\abdel\\OneDrive\\Desktop\\koloh\\4th year\\targama.txt','a',encoding='utf-8')

# string = "sky is clear"
lines=file1.readlines()[33728:]
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
count = 20
for string in lines:
    while count:
        try:
            # driver = webdriver.Chrome()
            url= "https://translate.google.com/?sl=en&tl=ar&text="+urllib.parse.quote(string)+"&op=translate"
            # driver.maximize_window()
            driver.get(url)
            time.sleep(1)

            text=driver.find_element_by_class_name("VIiyi").get_attribute("innerText")
            # reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
            # bidi_text = get_display(reshaped_text)    
            # araby.normalize_hamza(text,method="tasheel")
            file2.write(text)
            file2.write("\n")
        except Exception as e:
            # print(e)
            # count -=1
            continue
        # count =20
        break

file1.close()
file2.close()
driver.quit()
end = time.time()
print("time taken : ",end-start)
# content = driver.page_source.encode('utf-8').strip()
# soup = BeautifulSoup(content,"html.parser")
# officials = soup.find_all("div", {"class": "VIiyi"})

# for entry in officials:
#     print(str(entry))


# from pyarabic.unshape import unshaping_text
# TEXTS = u'لو والحيـاة مريرة   وليتك ترضى والانـــام غضاب '
# print(unshaping_text(TEXTS))