#!/bin/python3
from PIL import Image
import pyheif
import os
import sys

def translate(path_to_files, path_to_export, file_name):
    heif_file = pyheif.read(path_to_files + file_name)

    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(path_to_export + file_name[:-5] + ".jpg", "JPEG")
def return_files(path_to_files):
    raw_list = os.listdir(path_to_files)
    list = []
    for x in raw_list:
        if x.endswith('.heic') == True:
            list.append(x)
    return list
def main():
    if len(sys.argv) == 3:
        file_list = return_files(sys.argv[1])
        for x in file_list:
            translate(path_to_files=sys.argv[1] + '/', path_to_export=sys.argv[2]+ '/', file_name=x)
    else:
        path_to_files = input('Path to files: ')
        path_to_export = input('Path to export: ')
        file_list = return_files(path_to_files)
        for x in file_list:
            translate(path_to_files=path_to_files + '/', path_to_export=path_to_export + '/', file_name=x)
if __name__=="__main__":
    main()
