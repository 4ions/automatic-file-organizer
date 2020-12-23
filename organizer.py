#!/usr/bin/python3
import os
import time
import shutil

#trae el directorio actual donde se ejecuta el comando
pwd = str(os.getcwd())
#lista todos los archivos del directorio actual
list = os.listdir()


for i in list:
    temp = str(time.ctime(os.path.getmtime(i)))
    date = temp[4:7] + "_" + temp[8:10]
    if os.path.isdir(pwd + "/" + date + "/"):
        if i == "organizer.py":
            print("...")
        else:
            print("Moving...  {}".format(i))
            shutil.move(pwd+"/"+i,pwd+"/"+ date + "/")            
        
    else:
        os.mkdir(date)
        print("Created directory")
        if os.path.isdir(pwd + "/" + date + "/"):
            if i == "organizer.py":
                print("...")
            else:
                print("Moving.. {}".format(i))
                shutil.move(pwd+"/"+i,pwd+"/"+ date + "/")
        
#BUGS ACUTALES: Si se ejectuta dos veces, movera todos los y carpetas creadas a la carpeta del dia de hoy!!! :(
#ES un bug? lo normal es que si se ejecuta re organice nuevamente...., no?


 
