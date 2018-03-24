#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:17:20 2018

@author: francescourbani
"""

import sys
import math
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = sys.argv[1]
# FILE_NAME = "../Draft2.fft.txt"

with open(FILE_NAME, "r") as f:
	first_row = f.readline()

TITLE = first_row.split('\t')[1][:-1]

f_  = []
re_ = []
im_ = []

with open(FILE_NAME, "r") as f:
	next(f) # skip header
	for line in f:
		f_.append(float(line.split('\t')[0]))
		re_.append(float(line.split('\t')[1].split(',')[0]))
		im_.append(float(line.split('\t')[1].split(',')[1][:-1]))	
		
re_ = np.array(re_)
im_ = np.array(im_)
fft_ = re_ + 1j*im_


# plotting
plt.figure()

plt.subplot(211)
plt.title(TITLE)
plt.yscale('log')
plt.xscale('log')
plt.grid(True)
plt.plot(f_,np.abs(fft_), label="mag("+TITLE+")")
plt.legend()


plt.subplot(212)
plt.xscale('log')
plt.grid(True)
plt.xlabel("Frequency (Hz)")
plt.plot(f_,np.degrees(np.angle(fft_)), label="phase("+TITLE+")")
plt.legend()

plt.show()
