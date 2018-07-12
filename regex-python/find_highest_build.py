#!/usr/bin/env python3

import os
import random
import re

#Regex Pattern x.y.z that will match potential build nos in /Build-x.y.z.dmg
#The First Digit 'x' will always be present and goes up to 999
#The Second Digit 'y' is optional and goes up to 99
#The Third Digit 'z' is optional and goes up to 99
PATTERN = '([0-9]{1,3}).([0-9]{,2}).([0-9]{,2})'

#Absolute Path to the directory that contains the build files
DIR_NAME = '/Users/butterflyeffect/PyProjects/temp'

#Function that creates random build files in dir_name
#Build files will be of the format Build-x.y.z.dmg
#Where x.y.z follows the pattern above
def create_build_files(dir_name):
    ver = ''
    for i in range(100):
        v1 = random.randrange(1,1000)
        v2 = random.randrange(1,100)
        v3 = random.randrange(1,100)
        ver = str(v1) + '.' + str(v2) + '.' + str(v3)
        file_name = "Build-" + ver + ".dmg"
        abs_fname = os.path.join(dir_name, file_name)
        if not os.path.exists(abs_fname):
            fhand = open(abs_fname, 'w')
            fhand.write(ver)
            fhand.close()

#Function
def get_highest_build_no(dir_name):
    build_regex = re.compile(PATTERN)
    max_ver = None
    for folder, subfolder, files in os.walk(dir_name):
        for file in files:
            match_obj = build_regex.search(file)
            if (match_obj is not None):
                ver = match_obj.group(1)
                ver_str = ver
                if (match_obj.group(2) is not ''):
                    ver = ver + "." + match_obj.group(2)
                    ver_str = ver
                if (match_obj.group(3) is not ''):
                    ver_str = ver_str + "." + match_obj.group(3)
                    ver = ver + match_obj.group(3)
            ver = float(ver)
            if (max_ver is None or ver > max_ver):
                max_ver = ver
                max_ver_str = ver_str
    print(max_ver_str)

#Function to find the largest build number from the build files in dir_name
#Loop through the list of files and get x.y.z from the filename
#Convert the string x.y.z into float x.yz 
#And keep track of the max float 'x.yz' seen so far
def print_highest_build_no(dir_name):
    build_regex = re.compile(PATTERN)
    max_ver = None
    for folder, subfolder, files in os.walk(dir_name):
        for file in files:
            ver = build_regex.findall(file)
            if (len(ver) > 0):
                ver_num = ver[0][0]
                ver_str = ver_num
                if (ver[0][1] is not ''):
                    ver_num = ver_num + "." + ver[0][1]
                    ver_str = ver_num
                if (ver[0][2] is not ''):
                    ver_num = ver_num + ver[0][2]
                    ver_str = ver_str + "." + ver[0][2]
            if (max_ver is None or ver_num > max_ver):
                max_ver = ver_num
                max_str = ver_str
    print(max_str)


#file_list = get_files_in_dir('/Users/butterflyeffect/PyProjects/temp')
#swap_files(file_list)
#create_build_files('/Users/butterflyeffect/PyProjects/temp')
#get_highest_build_no(DIR_NAME)
print_highest_build_no('/Users/butterflyeffect/PyProjects/temp')
