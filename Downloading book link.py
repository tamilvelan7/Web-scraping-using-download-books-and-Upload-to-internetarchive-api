from selenium import webdriver
web = webdriver.Chrome("C:\drivers\chromedriver.exe")
web.get("http://www.e-books-chennaimuseum.tn.gov.in/chennaimuseum/index.php?option=com_abook&view=search&Itemid=101")
while True:
    try:
        file = (web.find_elements_by_xpath('//h3[@class="book-title"]/a'))
        for files in file:
            folder=files.get_attribute("href")
            print(folder)
            f=open('tamilbooks.txt',"a")
            f.write(folder+'\n')
            f.close()
        web.find_element_by_link_text("»").click()
    except:
        break
web.close()
    
