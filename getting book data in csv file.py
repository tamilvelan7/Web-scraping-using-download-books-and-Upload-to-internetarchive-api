from selenium import webdriver
import csv
web = webdriver.Chrome("C:\drivers\chromedriver.exe")
f=open('tamilbooks.txt',"r")
tamil=f.readlines()
with open('book_data8.csv','w',newline='')as bok:
    cols = ["title","licenseurl","Category", "Author", "Editor", "Pages", "Price", "Library", "Location", "Year"]
    w=csv.DictWriter(bok,fieldnames=cols)
    w.writeheader()

book_data={}  
for tamils in tamil:

    web.get(tamils)
    file=web.find_elements_by_xpath('//div[@class="bookdetails"]/div')
    book_name=web.find_element_by_xpath('//h6')
    book_link=web.find_elements_by_xpath('//a[@class="tooltip"]')
    #print(book_name.text)
    
    hit=[]
    book_data["title"]=(book_name.text)
    for bk in book_link:
        bkf=bk.get_attribute("href")
        book_data["licenseurl"]=bkf

    for files in file:
        # print(files.text)
        data=(files.text)
        splitted_string = data.split(':')
        bk=splitted_string[0]
        bk1=splitted_string[1]
        book_data[bk]=bk1
    with open('book_data8.csv','a',newline='')as bok:
        cols = ["title","licenseurl","Category", "Author", "Editor", "Pages", "Price", "Library", "Location", "Year"]
        w=csv.DictWriter(bok,fieldnames=cols)
       
        w.writerow(book_data)
    
bok.close()
web.close()