

#Rename files in a directory in their inverse sorted order
#Eg: a dir with files 1 - 10 will have the following state
#File 10 renamed as File 1 and so on file 5 remains the same
#A temp file is used as a 'swap' to save the original file 
#before it is renamed so that we dont lose data 

import os
import logging

logging.basicConfig(filename = 'SwapFiles_log.txt', 
                    level = logging.DEBUG, 
                    format = '%(asctime)s-%(levelname)s-%(message)s')

def get_files_in_dir(dirname):
    file_list = []
    for folder, subfolder, filenames in os.walk(dirname):
        for file in filenames:
            file_list.append(os.path.join(dirname, file))
    file_list.sort()
    logging.debug('Filename List')
    logging.debug('%s' % filenames)
    logging.debug('%s' % file_list)
    return file_list


def swap_files(file_names):
    file_map = {}
    num_files = len(file_names)
    j = 0
    dir_name = os.path.dirname(file_names[j])
    tmp_file = os.path.join(dir_name, 'tmp')
    while (j < num_files/2):
        logging.debug('Swapping %s %s' % (file_names[j], file_names[-(j+1)]))
        os.rename(file_names[j], tmp_file)
        os.rename(file_names[-(j+1)], file_names[j])
        os.rename(tmp_file, file_names[-(j+1)])
        j += 1

logging.debug('Start of Program')

file_list = get_files_in_dir('/Users/butterflyeffect/PyProjects/temp')
swap_files(file_list)

logging.debug('End of Program')