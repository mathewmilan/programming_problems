'''
Created on Nov 26, 2017
We want to find files that have the exact same contents, byte for byte, within a given directory. Write a function that takes a path and returns a list of lists or sets. Each set should contain files that have the same content.

An example output is for the input '/foo/' is:

[
   ['/foo/bar.png', '/foo/images/foo.png'],
   ['/foo/file.tmp', '/foo/other.temp', '/foo/temp/baz/that.foo']
]
@author: butterflyeffect
'''

import os
import subprocess
import pprint
import logging
from hashlib import sha256

logging.basicConfig(filename = 'CompareFiles_log.txt', 
                    level = logging.DEBUG, 
                    format = '%(asctime)s-%(levelname)s-%(message)s')

def get_files_in_dir(dir_name):
    file_list = []
    for folder, subfolder, filenames in os.walk(dir_name):
        for file in filenames:
            file_list.append(os.path.join(dir_name, file))
    logging.debug('Absolute Filename List')
    logging.debug('%s' % file_list)
    return file_list


def hash_files(filename):
    block_size = 65536 # 2 ** 16
    with open(filename, 'rb') as bfhand:
        hasher = sha256()
        while True:
            buf = bfhand.read(block_size)
            if not buf:
                break
            hasher.update(buf)
    return hasher.hexdigest()


def compare_files_in_dir(filenames):
    file_map = {}
    for file in filenames:
        fhash = hash_files(file)
        if (fhash in file_map):
            file_map[fhash].append(file)
        else:
            file_map[fhash] = [file]
    pprint.pprint(file_map)


logging.debug('Start of Program')

file_list = get_files_in_dir('/Users/butterflyeffect/PyProjects/files')
compare_files_in_dir(file_list)

logging.debug('End of Program')