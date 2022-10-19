# argv[1] single / folder

# if single:
# argv[2] : filename
# argv[3] : destination folder

# if folder :
# argv[2] : source folder
# argv[3] : destination folder

# e.g. 1: python resize.py folder ./SourceImages ./Destination/
# e.g. 2: python resize.py single ./SourceImages/img01.tga ./Destination/

from PIL import Image
import sys
import numpy as np
import os

sizeArray = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]

def main():
    if(len(sys.argv)!=4):
        print("参数数量不为4")
    else:
        if(sys.argv[1]=="folder"):
            g = os.walk(sys.argv[2])
            for path,dir_list,file_list in g:
                for file_name in file_list:
                    current_file = os.path.join(path,file_name)
                    print("Resizing:",current_file)
                    resize(current_file)
        elif(sys.argv[1]=="single"):
            if(os.path.isabs(sys.argv[2])):
                resize(sys.argv[2])
            else:
                resize(os.path.abspath(sys.argv[2]))


def resize(filepath):
    img = Image.open(filepath)
    old_width = img.size[0]
    old_height = img.size[1]

    width_diff = [abs(x - old_width) for x in sizeArray]
    height_diff = [abs(x - old_height) for x in sizeArray]
    new_width = sizeArray[np.argmin(width_diff)]
    new_height = sizeArray[np.argmin(height_diff)]
    print("Image Size:(",old_width,",",old_height,")")
    print("New Size:(",new_width,",",new_height,")")

    img_resized = img.resize((new_width, new_height),Image.ANTIALIAS)
    path,filename = os.path.split(filepath)
    img_resized.save(os.path.join(sys.argv[3],filename))


main()