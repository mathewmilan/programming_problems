#!/usr/bin/python

# import os
import re
import subprocess

#List all the spot instances supported by AWS
HELP_PATTERN = '(--instance-types \(list\)(\r\n|\n.*)*--product-descriptions)'
INSTYPE_PATTERN = '([a-z]+\d\.\d*[a-z]+)'
spot_history_output = subprocess.check_output(
    "aws ec2 describe-spot-price-history help",
    stderr=subprocess.STDOUT,
    shell=True)
print spot_history_output
instance_type_list = re.findall(INSTYPE_PATTERN, spot_history_output)
instance_type_set = set(instance_type_list)

print sorted(instance_type_set)
