import os
import sys
from classes.ppm import PPM

def get_file(file_name):
    os.system("if [ ! -d .tempICFMS ]; then mkdir .tempICFMS; fi")              # creates .tempICFMS folder if not exists (only on linux) 
    os.system("convert " + file_name + " -compress none .tempICFMS/temp.ppm")   # uses image-magik convert to .ppm P3

def prepare_PPM():
    file = open(".tempICFMS/temp.ppm", "r")
    a = file.readline()
    b = file.readline()
    abc = [int(n) for n in b.split()]
    c = file.readline()

    test = PPM(abc[0], abc[1], int(c))
    test.show()

    return file, test

def process_PPM(file, test):
    new_file = open(".tempICFMS/result.ppm", "w")
    new_file.write(test.id+'\n')
    new_file.write(str(test.size1)+' '+str(test.size2)+'\n')
    new_file.write(str(test.comp)+'\n')

    i = 0
    while(True):
        d = file.readline()
        if(d == ''):
            break
        bcd = [int(n) for n in d.split()]
        #bcd = [i+100 for i in bcd]
        i+=1
        print(i)
        #change_PPM(bcd)
        #crop_PPM(bcd, test)
        
        bcd = str(bcd).replace('[', '')
        bcd = bcd.replace(']', '')
        new_file.write(bcd.replace(',', '')+'\n')

    file.close()
    new_file.close()

def change_PPM(rgb):
    i = 0
    while(i < len(rgb)):
        rgb[i+2]=0
        i+=3

def crop_PPM(rgb, ppm):
    i = 0
    cont = 100
    while(i < len(rgb)):
        print()

def save(file_name):
    temp = file_name.split(".")
    if(len(temp) == 1):
        file_name = temp[0] + ".ppm"
        print(file_name)

    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    output_file = open(file_name, "w")

    if(temp[len(temp)-1] == "jpg" or temp[len(temp)-1] == "png" or temp[len(temp)-1] == "jpeg"):
        os.system("convert .tempICFMS/result.ppm " + file_name)
    else:
        os.system("mv .tempICFMS/result.ppm " + file_name)

def image_processing():
    fileList = sys.argv
    fileList.pop(0)
    if len(fileList) == 0:
        print("fatal error: no input files\nPlease insert all input files separated by a blank space after program name")
        return
    for i,file_name in enumerate(fileList):
        get_file(file_name)
        file, ppm = prepare_PPM()
        process_PPM(file, ppm)

        dirs = file_name.split('/')
        dirs.pop()
        direc = ''
        if len(dirs) > 0:
            direc = str(dirs).replace('[', '').replace(']', '').replace(',', '/').replace('\'', '') # get directory from file_name

        save(direc + "/result/out" + str(i) + "." + str(file_name.split('.').pop()))  

if(__name__ == "__main__"):
    image_processing()
