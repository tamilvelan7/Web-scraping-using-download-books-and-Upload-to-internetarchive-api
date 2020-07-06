from selenium import webdriver
web = webdriver.Chrome("C:\drivers\chromedriver.exe")
f=open('tamilbooks.txt',"r")
tamil=f.readlines()
for tamils in tamil:
    web.get(tamils)
    file =web.find_elements_by_xpath('//a[@class="tooltip"]')
    for files in file:
            folder=files.get_attribute("href")
            print(folder)
            f=open('tamilpdflink.txt',"a")
            f.write(folder+'\n')
            f.close()
web.close()
