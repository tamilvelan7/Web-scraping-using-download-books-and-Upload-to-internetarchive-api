from internetarchive import upload
import csv
x=open('upload.txt',"r")
file=x.read()
with open('book_data.csv','r') as files:
    data=csv.DictReader(files)
    for dataa in data:
        print(dataa)
        # upload('tamilvelanpython',file,metadata=dataa,verbose=True,queue_derive=False)