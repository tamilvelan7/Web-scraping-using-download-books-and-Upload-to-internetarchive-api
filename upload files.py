from internetarchive import upload
print("uploading files...")
x=open('upload.txt',"r")
file=x.read()
uploadfile=upload('tamilvelanpython',file)
print("Finished")