import os
from classes.ppm import PPM

def get_file():

    abc = []
    file_name = input("Type the file name > ")
    os.system("mkdir .temp")
    os.system("convert " + file_name + " -compress none .temp/temp.ppm")

def prepare_PPM():

    file = open(".temp/temp.ppm", "r")
    a = file.readline()
    b = file.readline()
    abc = [int(n) for n in b.split()]
    c = file.readline()

    test = PPM(abc[0], abc[1], int(c))
    test.show()

    return file, test

def process_PPM(file, test):

    new_file = open(".temp/result.ppm", "w")
    new_file.write(test.id+'\n')
    new_file.write(str(test.size1)+' '+str(test.size2)+'\n')
    new_file.write(str(test.comp)+'\n')

    while(True):
        d = file.readline()
        if(d == ''):
            break
        bcd = [int(n) for n in d.split()]
        #bcd = [i+100 for i in bcd]
        i = 0
        while(i < len(bcd)):
            bcd[i+2]=0
            i+=3
        bcd = str(bcd).replace('[', '')
        bcd = bcd.replace(']', '')
        new_file.write(bcd.replace(',', '')+'\n')

    file.close()
    new_file.close()

def save(file_name):
    temp = file_name.split(".")
    if(len(temp) == 1):
        file_name = temp[0] + ".ppm"
        print(file_name)

    output_file = open(file_name, "w")

    if(temp[len(temp)-1] == "jpg" or temp[len(temp)-1] == "png" or temp[len(temp)-1] == "jpeg"):
        os.system("convert .temp/result.ppm " + file_name)
    else:
        os.system("mv .temp/result.ppm " + file_name)

def image_processing():
    get_file()
    file, ppm = prepare_PPM()
    process_PPM(file, ppm)

    file_name = input("Type the output file name > ")
    save(file_name)


if(__name__ == "__main__"):
    image_processing()