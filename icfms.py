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
    d = ""
    while True:
        d = file.readline()
        if d == '':
            break
        bcd = [int(n) for n in d.split()]
        test.pixels.extend(bcd)

    file.close()
    test.show()

    return test

def crop_PPM(ppm):
    i = j = 0
    m_x = m_y = 0
    crop_x = crop_y = 0
    limit = 10
    while i < ppm.size2:
        j = 0
        while j < ppm.size1*3:
            if ppm.pixels[j + ppm.size1*3*i] > 240:
                crop_x += 1
            else:
                crop_x = 0
            
            if crop_x >= limit*3:
                m_x += j - limit*3
                break
            j += 1

        if j-limit*3 <= 5:
            crop_y += 1
        else:
            crop_y = 0

        if crop_y >= limit:
            m_y = i
            break
        i += 1
    
    # m_x = m_x/i

    print(m_x, m_y, i, j)

def save(file_name, ppm):
    new_file = open(".tempICFMS/result.ppm", "w")
    new_file.write(ppm.id+'\n')
    new_file.write(str(ppm.size1)+' '+str(ppm.size2)+'\n')
    new_file.write(str(ppm.comp)+'\n')
    new_file.write(str(ppm.pixels).replace('[', '').replace(']', '').replace(',', '')+'\n')
    new_file.close()

    temp = file_name.split(".")
    if len(temp) == 1:
        file_name = temp[0] + ".ppm"
        print(file_name)

    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    output_file = open(file_name, "w")

    if temp[len(temp)-1] == "jpg" or temp[len(temp)-1] == "png" or temp[len(temp)-1] == "jpeg":
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
        ppm = prepare_PPM()
        crop_PPM(ppm)

        dirs = file_name.split('/')
        dirs.pop()
        direc = ''
        if len(dirs) > 0:
            direc = str(dirs).replace('[', '').replace(']', '').replace(',', '/').replace('\'', '') # get directory from file_name

        save(direc + "/result/out" + str(i) + "." + str(file_name.split('.').pop()), ppm)  

if(__name__ == "__main__"):
    image_processing()
