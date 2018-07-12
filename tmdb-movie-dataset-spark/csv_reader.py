#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:50:12 2018

@author: butterflyeffect
"""

import csv
moviesFile = open("../tmdb_5000_movies.csv")
moviesReader = csv.reader(moviesFile)
moviesData = list(moviesReader)

for i in range(2):
    print moviesData[i][1]
    print moviesData[i][4]
    print moviesData[i][9]
    print moviesData[i][10]
    print moviesData[i][14]
