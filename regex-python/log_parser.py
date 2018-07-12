#!/usr/bin/env python3

import re
import datetime, time
import pprint

HOST_PATTERN = 'host="([0-9A-Za-z]+.[a-z]{3})"'
SVC_PATTERN = 'service=([0-9]+)ms'
TS_PATTERN = '([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6}\+[0-9]{2}:[0-9]{2})'

LOG_FILE = '/home/butterflyeffect/Workspace/PyProjects/starwars/fixture.log'
OUT_FILE = '/home/butterflyeffect/Workspace/PyProjects/starwars/log_output.txt'


def get_host_info_for_time_period(log_file):
    host_map = {}
    host_regex = re.compile(HOST_PATTERN)
    svc_regex = re.compile(SVC_PATTERN)
    ts_regex = re.compile(TS_PATTERN)
    try:
        fhand = open(log_file)
    except:
        print('File cannot be opened: ', log_file)
        exit()
    for line in fhand:
        host_name = ''.join(host_regex.findall(line))
        svc_time = ''.join(svc_regex.findall(line))
        time_stamp = ''.join(ts_regex.findall(line))
        time_stamp = time_stamp.split('+')
        time_stamp_dt = datetime.datetime.strptime(time_stamp[0], "%Y-%m-%dT%H:%M:%S.%f")
        key = (time_stamp_dt, host_name)
        value = svc_time
        if (key in host_map.keys()):
            host_map[(key)][0] += 1
            host_map[(key)][1] += value
            if (value < host_map[(key)][2]):
                host_map[(key)][2] = value
            if (value > host_map[(key)][3]):
                host_map[(key)][3] = value
        else:
            host_map[(key)] = []
            host_map[(key)].append(1)
            host_map[(key)].append(value)
            host_map[(key)].append(value)
            host_map[(key)].append(value)
    return host_map

def write_host_info_to_file(out_file, host_map):
    fout = open(out_file, 'w')
    for key in sorted(host_map.keys()):
        print("%s,%s,%s,%s,%s,%s" 
              % (key[0].strftime("%Y-%m-%dT%H:%M"),
                 key[1], 
                 host_map[(key)][0],
                 host_map[(key)][1],
                 host_map[(key)][2],
                 host_map[(key)][3]
                )
              )
    return


host_info = get_host_info_for_time_period(LOG_FILE)
write_host_info_to_file(OUT_FILE, host_info)