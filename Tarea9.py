#Tarea 9

f = open("demofile1.txt", "a") # Append to an existing file
f.write("The file will include more text..")
f.close()
f2 = open("demofile2.txt", "w") # Creating and writing to a newfile
f2.write("demofile2 file created, with this content in!")
f2.close()

f3 = open("flag.txt","w")
f4 = open("flag.txt","r")
print(f4.read())

# El resultado es un print vacío ya que nuestro archivo está vacío





