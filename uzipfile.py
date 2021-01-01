from zipfile import ZipFile 
  
file_name = "Student.zip"
  
with ZipFile(file_name, 'r') as zip: 
   
	zip.printdir() 
	print('Extracting all the files now...') 
	zip.extractall() 
	print('Done!') 
	filename="extract.txt"
	file=open(filename,'w')
	file.write(file_name)
	file.close()
