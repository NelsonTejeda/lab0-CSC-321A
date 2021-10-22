#!/usr/bin/env python
# Stable Matching
# Created by: Nelson Tejeda
#Date: 11/30/2021
# Purpose: runs stableSort.py more than 11 times and makes a fit graph for each point created
#Input: none
#Output: graph

import os
import time
import subprocess


for i in range(1000, 5001, 200):
    os.system('python gs1.py {}'.format(i))

proc = subprocess.Popen(['gnuplot', '-p'],
                        shell=True,
                        stdin=subprocess.PIPE,
                        )
proc.stdin.write(b'y(x) = a0 + a1 * x + a2 * x**2\n')
proc.stdin.write(b'a0 = 1\n')
proc.stdin.write(b'a1 = 0.1\n')
proc.stdin.write(b'a2 = 1\n')
proc.stdin.write(b'fit y(x) "data.txt" via a0, a1, a2\n')
proc.stdin.write(b'plot y(x), "data.txt"\n')

# time.sleep(3)
# os.system('gnuplot')
# os.system('y(x) = a0 + a1 * x + a2 * x**2')
# os.system('a0 = 1')
# os.system('a1 = 0.1')
# os.system('a2 = 1')
# os.system('fit y(x) "output.txt" via a0, a1, a2')
# os.system('plot y(x), "output.txt"')
